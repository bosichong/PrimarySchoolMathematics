<template>
  <div>
    <ElFormItem label="几步运算?">
      <el-radio-group v-model="formData.step" @change="changeStep">
        <el-radio-button v-for="o in stepOptions" :label="o.key" :disabled="o.disabled">{{ o.label }}</el-radio-button>
      </el-radio-group>
      <ElButton type="primary" style="margin-left: 6px;" @click="openOptionsDrawer">其他设置</ElButton>
    </ElFormItem>

    <template v-for="item, index in formData.formulaList">
      <ElFormItem v-if="item.operators" :label="`第${index}步运算符号选择`" :prop="`formulaList.${index}.operators`"
        :rules="requiredRule">
        <el-checkbox-group v-model="item.operators">
          <el-checkbox v-for="o in operatorOptions" :label="o.key">{{ o.label }}</el-checkbox>
        </el-checkbox-group>
      </ElFormItem>

      <ElFormItem :label="`算数项${index + 1}`">
        <ElRow :gutter="8">
          <ElCol :span="8">
            <ElFormItem :prop="`formulaList.${index}.min`" :rules="requiredNumberRule">
              <ElInput v-model.number="item.min">
                <template #prepend>最小值</template>
              </ElInput>
            </ElFormItem>
          </ElCol>
          <ElCol :span="8">
            <ElFormItem :prop="`formulaList.${index}.max`" :rules="requiredNumberRule">
              <ElInput v-model.number="item.max">
                <template #prepend>最大值</template>
              </ElInput>
            </ElFormItem>
          </ElCol>
        </ElRow>
      </ElFormItem>
    </template>

    <ElFormItem label="运算结果">
      <ElRow :gutter="8">
        <ElCol :span="8">
          <ElFormItem prop="resultMinValue"
            :rules="[{ required: true, message: '请填写运算结果最小值' }, { type: 'number', message: '请填写数字' }]">
            <ElInput v-model.number="formData.resultMinValue">
              <template #prepend>最小值</template>
            </ElInput>
          </ElFormItem>
        </ElCol>
        <ElCol :span="8">
          <ElFormItem prop="resultMaxValue"
            :rules="[{ required: true, message: '请填写运算结果最大值' }, { type: 'number', message: '请填写数字' }]">
            <ElInput v-model.number="formData.resultMaxValue">
              <template #prepend>最大值</template>
            </ElInput>
          </ElFormItem>
        </ElCol>
      </ElRow>
    </ElFormItem>

    <ElFormItem prop="numberOfFormulas"
      :rules="[{ required: true, message: '请填写口算题数量' }, { type: 'number', message: '请填写数字' }]">
      <ElRow :gutter="20">
        <ElCol :span="14">
          <ElInput v-model.number="formData.numberOfFormulas">
            <template #prepend>口算题数量</template>
          </ElInput>
        </ElCol>
      </ElRow>
    </ElFormItem>

    <ElFormItem>
      <ElButton type="primary" @click="append">添加口算题</ElButton>
      <ElButton @click="clear">清空口算题</ElButton>
      <el-button type="success" @click="addConfiguration">将当前参数保存为配置</el-button>
    </ElFormItem>

    <OptionsDrawer v-model:visible="optionsDrawerVisible" v-model:formulasFormData="formData" />
  </div>
</template>

<script setup>
import { computed, ref, unref, toRaw, getCurrentInstance } from 'vue';
import { v4 as uuidv4 } from "uuid";
import { cloneDeep } from "lodash";
import ConfigStorage from '@/utils/configStorage';
import { OptionsDrawer } from "@/components/home";

const { proxy } = getCurrentInstance()

const props = defineProps({
  formulasFormData: {
    type: Object
  },
  papers: {
    type: Array
  },
  refForm: {
    type: Object
  },
  configurations: Array
})

const emit = defineEmits(['update:formulasFormData', 'update:papers', 'add-configuration'])

const formData = computed({
  get() {
    return props.formulasFormData
  },
  set(val) {
    emit('update:formulasFormData', val)
  }
})

const paperList = computed({
  get() {
    return props.papers
  },
  set(val) {
    emit('update:papers', val)
  }
})

const operatorOptions = [
  { key: 1, label: '+(加法)' },
  { key: 2, label: '-(减法)' },
  { key: 3, label: '×(乘法)' },
  { key: 4, label: '÷(除法)' }
]

const requiredRule = [
  { required: true, message: '此项为必填项' }
]
const requiredNumberRule = [
  { required: true, message: '此项为必填项' }, { type: 'number', message: '此项必须为数字' }
]


const stepOptions = computed(() => {
  // 多步运算时不能有余数
  const disabled = formData.value.remainder == '3'
  return [
    { key: '1', label: "一步运算", disabled: false },
    { key: '2', label: "两步运算", disabled },
    { key: '3', label: "三步运算", disabled }
  ]
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

const optionsDrawerVisible = ref(false)
const openOptionsDrawer = () => {
  optionsDrawerVisible.value = true
}

const append = () => {
  props.refForm?.validate((valid) => {
    if (!valid) return

    const { step, numberOfFormulas, whereIsResult, formulaList, resultMinValue, resultMaxValue } = cloneDeep(toRaw(formData.value))
    paperList.value.push({
      step, numberOfFormulas, whereIsResult, formulaList, resultMinValue, resultMaxValue
    })
  })
}

const clear = () => {
  paperList.value = []
}

const addConfiguration = () => {
  props.refForm?.validate((valid) => {
    if (!valid) return

    proxy.$messageBox.prompt('请给配置起个名字', '提示', {
      inputPattern: /^\S{1,10}$/,
      inputPlaceholder: '不能多于10个字符',
      inputErrorMessage: '配置名字不能为空且不能多于10个字符'
    }).then(({ value }) => {
      if (props.configurations?.length >= 10) {
        proxy.$message.error('最多只能保存10份配置！')
        return
      }

      const newId = uuidv4()
      new ConfigStorage().save(newId, value, toRaw(unref(formData)))
      proxy.$message.success('保存成功!')
      emit('add-configuration', newId)
    })
  })
}
</script>

<style lang="scss" scoped></style>