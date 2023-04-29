<template>
  <el-dialog v-model="currentVisible" fullscreen title="" :show-close="false" append-to-body :close-on-click-modal="false" @open="open"
    @closed="closed">
    <template #footer v-if="!isPrint">
      <el-button type="primary" @click="print">打印</el-button>
      <el-button @click="currentVisible = false">关闭</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed, defineComponent, nextTick } from 'vue';


const ccc = defineComponent({ template: "<h1>123</h1>" })

const props = defineProps({
  visible: {
    type: Boolean
  },
  source: {
    type: Object
  }
})

const emit = defineEmits(['update:visible'])

const currentVisible = computed({
  get() {
    return props.visible
  },
  set(val) {
    emit('update:visible', val)
  }
})

const open = async () => {

}

const closed = () => {

}

const isPrint = ref(false)
const print = () => {
  isPrint.value = true
  nextTick(() => {
    window.print()
  })
}
</script>

<style lang="scss" scoped>
.bottom {
  height: 70vh;
  /* 底部70% */
  background-color: #eee;
  position: relative;
}

.bottom iframe {
  position: absolute;
  top: 0;
  left: 50%;
  /* 横向居中 */
  transform: translateX(-50%);
  /* 横向居中 */
  width: 100%;
  height: 100%;
  border: none;
}
</style>