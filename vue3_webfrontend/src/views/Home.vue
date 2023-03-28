<template>
  <div>
    <ElForm ref="refForm" :model="formData" :rules="formRules" label-position="top">
      <ElFormItem label="几步运算?">
        <el-radio-group v-model="formData.step" @change="changeStep">
          <el-radio-button label="1">一步运算</el-radio-button>
          <el-radio-button label="2">两步运算</el-radio-button>
          <el-radio-button label="3">三步运算</el-radio-button>
        </el-radio-group>

        <ElButton type="primary" style="margin-left: 6px;" @click="openOptionsDrawer">其他设置</ElButton>
      </ElFormItem>

      <template v-for="item, index in formData.formulaList">
        <ElFormItem v-if="item.operators" :label="`第${index}步运算符号选择`">
          <el-checkbox-group v-model="item.operators">
            <el-checkbox v-for="o in operatorOptions" :label="o.key">{{ o.label }}</el-checkbox>
          </el-checkbox-group>
        </ElFormItem>

        <ElFormItem :label="`算数项${index + 1}`">
          <ElRow :gutter="8">
            <ElCol :span="8">
              <ElInput v-model="item.min">
                <template #prepend>最小值</template>
              </ElInput>
            </ElCol>
            <ElCol :span="8">
              <ElInput v-model="item.max">
                <template #prepend>最大值</template>
              </ElInput>
            </ElCol>
          </ElRow>
        </ElFormItem>
      </template>

      <ElFormItem label="运算结果">
        <ElRow :gutter="8">
          <ElCol :span="8">
            <ElFormItem prop="resultMinValue">
              <ElInput v-model="formData.resultMinValue">
                <template #prepend>最小值</template>
              </ElInput>
            </ElFormItem>
          </ElCol>
          <ElCol :span="8">
            <ElFormItem prop="resultMaxValue">
              <ElInput v-model="formData.resultMaxValue">
                <template #prepend>最大值</template>
              </ElInput>
            </ElFormItem>
          </ElCol>
        </ElRow>
      </ElFormItem>

      <ElFormItem prop="numberOfFormulas">
        <ElRow :gutter="20">
          <ElCol :span="11">
            <ElInput v-model="formData.numberOfFormulas">
              <template #prepend>口算题数量</template>
            </ElInput>
          </ElCol>
          <ElCol :span="5">
            <el-button type="primary" @click="append">添加口算题</el-button>
          </ElCol>
          <ElCol :span="5">
            <el-button @click="clear">清空口算题</el-button>
          </ElCol>
        </ElRow>
      </ElFormItem>

    </ElForm>

    <template v-if="paperDescriptionList && paperDescriptionList.length">
      <p>当前口算题包含的内容</p>
      <div v-for="p in paperDescriptionList">
        <ElTag>{{ p }}</ElTag>
      </div>
    </template>

    <el-button :disabled="!paperList.length" type="primary" :loading="buttonLoading"
      @click="generate">点此生成口算题卷子</el-button>

    <OptionsDrawer v-model:visible="optionsDrawerVisible" v-model:formulasFormData="formData" />

    <PaperDownloadDialog v-model:visible="paperDownloadDialogVisible" />
  </div>
</template>

<script setup>
import { ref, onMounted, unref, toRaw, getCurrentInstance, computed } from 'vue';
import OptionsDrawer from "@/components/home/OptionsDrawer.vue";
import PaperDownloadDialog from "@/components/home/PaperDownloadDialog.vue";
import { generatePaper, loadConfiguration } from '@/apis/paper';

const { proxy } = getCurrentInstance()

const operatorOptions = [
  { key: 1, label: '+(加法)' },
  { key: 2, label: '-(减法)' },
  { key: 3, label: '×(乘法)' },
  { key: 4, label: '÷(除法)' }
]

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
  downloadPath: ''
})

const formRules = ref({
  resultMinValue: [{ required: true, message: '请填写运算结果最小值' },{ type: 'number', message: '请填写数字' }],
  resultMaxValue: [{ required: true, message: '请填写运算结果最大值' },{ type: 'number', message: '请填写数字' }],
  numberOfFormulas: [{ required: true, message: '请填写口算题数量' }]
})


const changeStep = (val) => {
  // 选择了新的几步运算后, 计算新值与旧值的差
  const difference = parseInt(val) - formData.value.formulaList.length + 1

  // 如果差是正数说明需要增加新的算数项,如果差是负数说明需要减去旧的算数项
  if (difference > 0) {
    for (let i = 1; i <= difference; i++) {
      formData.value.formulaList.push({ min: 1, max: 9, operators: [1] })
    }
  } else if (difference < 0) {
    formData.value.formulaList.splice(difference, Math.abs(difference))
  }
}

onMounted(async () => {
  console.log('少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了')

  // todo 调用api获取用户保存的配置
  const { downloadPath } = await loadConfiguration()
  formData.value.downloadPath = downloadPath
})

const optionsDrawerVisible = ref(false)
const openOptionsDrawer = () => {
  optionsDrawerVisible.value = true
}

const paperList = ref([])
const paperDescriptionList = computed(() => {
  return paperList.value.map(p => {
    return `${p.step}步计算题口算题${p.numberOfFormulas}道`
  })
})
const append = () => {
  refForm?.value?.validate((valid) => {
    if (!valid) return

    const { step, numberOfFormulas, whereIsResult, formulaList, resultMinValue, resultMaxValue } = formData.value
    paperList.value.push({ step, numberOfFormulas, whereIsResult, formulaList, resultMinValue, resultMaxValue })
  })
}

const clear = () => {
  paperList.value = []
}

const buttonLoading = ref(false)
const paperDownloadDialogVisible = ref(false)
const generate = async () => {
  try {
    buttonLoading.value = true
    const { data: { info } } = await generatePaper(toRaw(unref(formData)), toRaw(unref(paperList)))
    proxy.$message.success(info)

    paperDownloadDialogVisible.value = true
  } finally {
    buttonLoading.value = false
  }
}
</script>

<style lang="scss" scoped></style>