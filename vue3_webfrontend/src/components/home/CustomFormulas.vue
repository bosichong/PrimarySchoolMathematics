<template>
  <div>
    <p class="p-under">可以手动添加题目生成进试卷,比如之前的错题和需要加强的题目。乘法除法填写时可以用
      <ElTag size="small">*</ElTag> 和 <ElTag size="small">/</ElTag> 代替,程序会自动替换。不需要填写等号。
    </p>
    <ElFormItem v-for="item, index in formData.customFormulaList" :prop="`customFormulaList.${index}.formula`"
      :rules="requiredRule">
      <div class="formula">
        <ElInput v-model="item.formula" placeholder="例: 20 * 10"/>
        <el-icon v-show="formData.customFormulaList.length == (index + 1)" @click="add">
          <CirclePlusFilled />
        </el-icon>
        <el-icon v-show="formData.customFormulaList.length > 1" @click="remove(index)">
          <RemoveFilled />
        </el-icon>
      </div>
    </ElFormItem>

    <ElFormItem>
      <el-button type="primary" @click="append">添加口算题</el-button>
      <el-button @click="clear">清空口算题</el-button>
    </ElFormItem>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  formulasFormData: {
    type: Object
  },
  papers: {
    type: Array
  },
  refForm: {
    type: Object
  }
})

const emit = defineEmits(['update:formulasFormData', 'update:papers'])

const formData = computed({
  get() {
    return props.formulasFormData
  },
  set(val) {
    emit('update:formulasFormData', val)
  }
})

const requiredRule = [
  { required: true, message: '此项为必填项' }
]

const paperList = computed({
  get() {
    return props.papers
  },
  set(val) {
    emit('update:papers', val)
  }
})

const add = () => {
  props.refForm?.validate((valid) => {
    if (!valid) return
    formData.value.customFormulaList.push({ formula: '' })
  })
}

const remove = (index) => {
  formData.value.customFormulaList.splice(index, 1)
}

const append = () => {
  const customFormulaList = formData.value.customFormulaList.reduce((prev, cur) => {
    if (cur.formula) {
      const formula = cur.formula.replace('*', 'x').replace('/', '÷').trim() + ' ='
      prev.push({ formula })
    }
    return prev
  }, [])

  paperList.value.push({ customFormulaList, numberOfFormulas: customFormulaList.length })
}

const clear = () => {
  paperList.value = []
}
</script>

<style lang="scss" scoped>
.formula {
  display: flex;
  align-items: center;

  i {
    margin-left: 6px;
    font-size: 20px;
  }
}
</style>