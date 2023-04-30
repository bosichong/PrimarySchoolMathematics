<template>
  <el-dialog v-model="currentVisible" fullscreen title="" :show-close="false" append-to-body :close-on-click-modal="false"
    @open="open" @closed="closed">

    <div class="A4">
      <div class="sheet padding-10mm">
        <div>
          <h1>三年级下学期口算题</h1>
          <h3>姓名：__________</h3>
        </div>
        <div class="row">
          <div class="col33">
            <p>20+29=</p>
            <p>88+57=</p>
            <p>92-54=</p>
            <p>22+75=</p>
            <p>8+22=</p>
            <p>70-22=</p>
            <p>12+29=</p>
            <p>68-49=</p>
            <p>64+10=</p>
            <p>21+31=</p>
            <p>11+25=</p>
            <p>61-17=</p>
            <p>91-52=</p>
            <p>20+79=</p>
            <p>14+47=</p>
            <p>43-14=</p>
            <p>37-24=</p>
            <p>71-19=</p>
            <p>90-48=</p>
            <p>43+45=</p>
            <p>4+49=</p>
          </div>
          <div class="col33">
            <p>20+29=</p>
            <p>88+57=</p>
            <p>92-54=</p>
            <p>22+75=</p>
            <p>8+22=</p>
            <p>70-22=</p>
            <p>12+29=</p>
            <p>68-49=</p>
            <p>64+10=</p>
            <p>21+31=</p>
            <p>11+25=</p>
            <p>61-17=</p>
            <p>91-52=</p>
            <p>20+79=</p>
            <p>14+47=</p>
            <p>43-14=</p>
            <p>37-24=</p>
            <p>71-19=</p>
            <p>90-48=</p>
            <p>43+45=</p>
            <p>4+49=</p>
          </div>
          <div class="col34">
            <p>20+29=</p>
            <p>88+57=</p>
            <p>92-54=</p>
            <p>22+75=</p>
            <p>8+22=</p>
            <p>70-22=</p>
            <p>12+29=</p>
            <p>68-49=</p>
            <p>64+10=</p>
            <p>21+31=</p>
            <p>11+25=</p>
            <p>61-17=</p>
            <p>91-52=</p>
            <p>20+79=</p>
            <p>14+47=</p>
            <p>43-14=</p>
            <p>37-24=</p>
            <p>71-19=</p>
            <p>90-48=</p>
            <p>43+45=</p>
            <p>4+49=</p>
          </div>
        </div>
        <div style="page-break-after: always;"></div>
      </div>
    </div>

    <template #footer v-if="!isPrint">
      <el-button type="primary" @click="print">打印</el-button>
      <el-button @click="currentVisible = false">关闭</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed, defineComponent, nextTick } from 'vue';

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

<style lang="scss">
// @import url("https://cdnjs.cloudflare.com/ajax/libs/paper-css/0.3.0/paper.css");

@page {
  size: A4
}

.A4 {
  text-align: center;
}

.row {
  display: flex;
  width: 100%;
}

.col33 {
  width: 33%;
}

.col34 {
  width: 34%;
}</style>