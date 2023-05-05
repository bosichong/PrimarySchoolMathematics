<template>
  <div class="page-container">
    <ElRow :gutter="20">
      <ElCol :xs="24" :sm="16" :md="16" :lg="12" :xl="8">
        <ElForm ref="refForm" :model="formData" label-position="top">
          <ElFormItem label="生成模式">
            <el-radio-group v-model="formData.generateMode">
              <el-radio-button label="1">自动生成</el-radio-button>
              <el-radio-button label="2">手动添加</el-radio-button>
            </el-radio-group>
          </ElFormItem>

          <template v-if="formData.generateMode == '1'">
            <AutoGenerateFormulas v-model:formulas-form-data="formData" v-model:papers="paperList" :ref-form="refForm"
              :configurations="configurations" @add-configuration="addConfiguration" />
          </template>

          <template v-if="formData.generateMode == '2'">
            <CustomFormulas v-model:formulas-form-data="formData" v-model:papers="paperList" :ref-form="refForm" />
          </template>

          <template v-if="paperDescriptionList && paperDescriptionList.length">
            <ElFormItem label="当前口算题包含的内容">
              <div v-for="p in paperDescriptionList">
                <ElTag style="margin-right: 8px;">{{ p }}</ElTag>
              </div>
            </ElFormItem>
          </template>
        </ElForm>

        <el-button :disabled="!paperList.length" type="primary" size="large" :loading="buttonLoading"
          @click="generate">点此生成口算题卷子</el-button>
      </ElCol>
      <ElCol :xs="24" :sm="8" :md="8" :lg="8" :xl="8">
        <ConfigurationList v-model:active-index="activeConfigurationId" :configurations="configurations"
          @removed="refreshConfiguration" @selected="selectedConfiguration" @reset="refreshConfiguration" />
      </ElCol>
    </ElRow>

    <PrintPreviewDialog v-model:visible="printPreviewDialogVisible" />
  </div>
</template>

<script setup>
import { ref, onMounted, unref, toRaw, getCurrentInstance, computed } from 'vue';
import { CustomFormulas, AutoGenerateFormulas, ConfigurationList, PrintPreviewDialog } from "@/components/home";
import ConfigStorage from "@/utils/configStorage";
import { fileNameGeneratedRuleEnum, httpContentTypeExtensionsMappingEnum } from '@/utils/enum';
import { download } from "@/utils/download";
import { generatePaper } from '@/apis/paper';

const { proxy } = getCurrentInstance()

const refForm = ref(null)

const formData = ref({
  step: '1', // 几步运算
  numberOfFormulas: 30, // 口算题数量
  whereIsResult: '0', // 题型设置
  enableBrackets: false, // 启用括号
  carry: '1',
  abdication: '1',
  remainder: '2',
  solution: '0', // 解题方式
  numberOfPapers: 3, // 试卷数量
  numberOfPagerColumns: 3, // 试卷列数
  paperTitle: '小学生口算题', // 试卷标题
  paperSubTitle: '姓名：__________ 日期：____月____日 时间：________ 对题：____道', // 试卷副标题
  // 试题格式
  // min 算数项最小值 max 算数项最大值 operators 与上一步算数项使用的运算符号
  // 第一个算数项由于没有上一步故设置为null
  formulaList: [
    { min: 1, max: 9, operators: null },
    { min: 1, max: 9, operators: [1] },
  ],
  resultMinValue: 1, // 试题运行结果最小值
  resultMaxValue: 9, // 试题运行结果最大值
  generateMode: '1',
  customFormulaList: [
    { formula: '' }
  ],
  fileNameGeneratedRule: fileNameGeneratedRuleEnum.baseOnTitleAndIndex.key
})

const configurations = ref([])

onMounted(async () => {
  console.log('少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了')

  refreshConfiguration()
  const { data: config } = configurations.value[0] // todo

  formData.value.step = config.step
  formData.value.numberOfFormulas = config.numberOfFormulas
  formData.value.whereIsResult = config.whereIsResult
  formData.value.enableBrackets = config.enableBrackets
  formData.value.carry = config.carry
  formData.value.abdication = config.abdication
  formData.value.remainder = config.remainder
  formData.value.solution = config.solution
  formData.value.numberOfPapers = config.numberOfPapers
  formData.value.numberOfPagerColumns = config.numberOfPagerColumns
  formData.value.paperTitle = config.paperTitle
  formData.value.paperSubTitle = config.paperSubTitle
  formData.value.formulaList = config.formulaList
  formData.value.resultMinValue = config.resultMinValue
  formData.value.resultMaxValue = config.resultMaxValue
  formData.value.fileNameGeneratedRule = config.fileNameGeneratedRule
})

const paperList = ref([])
const paperDescriptionList = computed(() => {
  return paperList.value.map(p => {
    return p.customFormulaList && p.customFormulaList.length ? `自定义口算题${p.numberOfFormulas}道` : `${p.step}步计算题口算题${p.numberOfFormulas}道`
  })
})

const activeConfigurationId = ref('1')
const refreshConfiguration = () => {
  configurations.value = new ConfigStorage().loadAll()
}
const addConfiguration = (newId) => {
  activeConfigurationId.value = newId
  refreshConfiguration()
}
const selectedConfiguration = (configuration) => {
  console.log(configuration);

  const { data: config } = configuration
  formData.value.step = config.step
  formData.value.numberOfFormulas = config.numberOfFormulas
  formData.value.whereIsResult = config.whereIsResult
  formData.value.enableBrackets = config.enableBrackets
  formData.value.carry = config.carry
  formData.value.abdication = config.abdication
  formData.value.remainder = config.remainder
  formData.value.solution = config.solution
  formData.value.numberOfPapers = config.numberOfPapers
  formData.value.numberOfPagerColumns = config.numberOfPagerColumns
  formData.value.paperTitle = config.paperTitle
  formData.value.paperSubTitle = config.paperSubTitle
  formData.value.formulaList = config.formulaList
  formData.value.resultMinValue = config.resultMinValue
  formData.value.resultMaxValue = config.resultMaxValue
  formData.value.fileNameGeneratedRule = config.fileNameGeneratedRule
}

const printPreviewDialogVisible = ref(false)
const buttonLoading = ref(false)
const generate = async () => {
  try {
    buttonLoading.value = true
    const { data, headers } = await generatePaper(toRaw(unref(formData)), toRaw(unref(paperList)))
    proxy.$message.success('口算题生成完毕，准备开始下载！')

    const contentType = headers['content-type']
    const fileExtensions = httpContentTypeExtensionsMappingEnum[contentType.toLowerCase()]
    const fileName = `${formData.value.paperTitle}.${fileExtensions}`

    download(data, fileName)

  } finally {
    buttonLoading.value = false
  }
}
</script>

<style lang="scss" scoped></style>