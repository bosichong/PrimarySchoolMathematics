<template>
  <div>
    <p>已保存配置列表</p>
    <ElCard v-for="c in configurations" style="margin-bottom: 20px;" :shadow="'hover'" @click="handle(c.id)">
      <!-- 是否选中 -->
      {{ c.name }}
      <el-icon v-if="configurations && configurations.length > 1" @click="remove(c.id)">
        <CircleCloseFilled />
      </el-icon>
    </ElCard>
  </div>
</template>

<script setup>
import { getCurrentInstance } from 'vue';
import configStorage from '@/utils/configStorage';
import { cloneDeep } from 'lodash';

const { proxy } = getCurrentInstance()

const props = defineProps({
  configurations: Array
})

const emits = defineEmits(['removed', 'selected'])

const remove = (id) => {
  new configStorage().remove(id)
  proxy.$message.success('删除成功!')
  emits('removed')
}

const handle = async (id) => {
  try {
    await proxy.$messageBox.confirm('确定加载吗? 注意未保存的参数将会丢失!', '提示', { type: 'warning' })
    const c = props.configurations.find(p => p.id == id)
    emits('selected', cloneDeep(c))
  } catch (error) {

  }
}

</script>

<style lang="scss" scoped></style>