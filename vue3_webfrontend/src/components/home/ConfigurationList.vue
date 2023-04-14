<template>
  <div>
    <div class="flex justify-between">
      <p class="text-base mb-5">已保存配置列表</p>
      <ElButton type="danger" size="small" @click="reset">重置配置</ElButton>
    </div>
    <ElCard v-for="c in configurations" :class="{ active: c.id == activeConfigurationId }" class="mb-3" :shadow="'hover'"
      @click="select(c.id)">
      <div class="flex justify-between items-center cursor-pointer">
        <!-- 是否选中 -->
        <p class="text-sm">{{ c.name }}</p>
        <el-icon v-if="configurations && configurations.length > 1" @click.stop="remove(c.id)">
          <CircleCloseFilled class="text-xl text-sky-600" />
        </el-icon>
      </div>
    </ElCard>
  </div>
</template>

<script setup>
import { getCurrentInstance, ref, computed, watch } from 'vue';
import ConfigStorage from '@/utils/configStorage';
import { cloneDeep } from 'lodash';

const { proxy } = getCurrentInstance()

const props = defineProps({
  activeIndex: {
    type: String,
    default: '1'
  },
  configurations: Array
})

const emits = defineEmits(['removed', 'selected', 'reset', 'update:activeIndex'])

const activeConfigurationId = computed({
  get() {
    return props.activeIndex
  },
  set(val) {
    emits('update:activeIndex', val)
  }
})

const remove = async (id) => {
  await proxy.$messageBox.confirm('确定删除吗? ', '提示', { type: 'warning' })
  new ConfigStorage().remove(id)
  proxy.$message.success('删除成功!')
  emits('removed')
}

const reset = () => {
  const configStorage = new ConfigStorage()
  configStorage.clear()

  // 如果目前选中的是默认配置
  if (activeConfigurationId.value == '1') {
    proxy.$message.success('重置成功')
    emits('reset')
  } else {
    const c = props.configurations.find(p => p.id == '1')
    activeConfigurationId.value = '1'
    proxy.$message.success('重置成功')
    emits('reset')
    emits('selected', cloneDeep(c))
  }
}

const select = async (id) => {
  try {
    await proxy.$messageBox.confirm('确定加载吗? 注意未保存的参数将会丢失!', '提示', { type: 'warning' })
    activeConfigurationId.value = id
  } catch (error) {
  }
}

watch(() => props.activeIndex, async (val) => {
  const c = props.configurations.find(p => p.id == val)
  emits('selected', cloneDeep(c))
})

</script>

<style lang="scss" scoped>
.active {
  @apply bg-sky-100;
}
</style>