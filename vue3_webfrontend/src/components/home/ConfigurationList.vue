<template>
  <div>
    <p>已保存配置列表</p>
    <ElCard v-for="c in configurations" style="margin-bottom: 20px;" class="card" :shadow="'hover'" @click="handle(c.id)">
      <div class="card-item">
        <!-- 是否选中 -->
        {{ c.name }}
        <el-icon v-if="configurations && configurations.length > 1" @click.stop="remove(c.id)">
          <CircleCloseFilled />
        </el-icon>
      </div>
    </ElCard>
  </div>
</template>

<script setup>
import { getCurrentInstance, ref } from 'vue';
import configStorage from '@/utils/configStorage';
import { cloneDeep } from 'lodash';

const { proxy } = getCurrentInstance()

const props = defineProps({
  configurations: Array
})

const emits = defineEmits(['removed', 'selected'])

const activeConfigurationId = ref('')

const remove = (id) => {
  new configStorage().remove(id)
  proxy.$message.success('删除成功!')
  emits('removed')
}

const handle = async (id) => {
  try {
    await proxy.$messageBox.confirm('确定加载吗? 注意未保存的参数将会丢失!', '提示', { type: 'warning' })
    const c = props.configurations.find(p => p.id == id)
    activeConfigurationId.value = id
    emits('selected', cloneDeep(c))
  } catch (error) {

  }
}

</script>

<style lang="scss" scoped>
.card {

  &.active {
    background-color: aqua;
  }

  .card-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;

    i {
      font-size: 20px;
      color: blue;
    }
  }
}
</style>