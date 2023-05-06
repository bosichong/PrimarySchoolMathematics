<template>
  <div :class="{ 'preview': !isPrinting }">
    <div class="A4">
      <div class="sheet padding-10mm" :class="{ 'sheet-shadow': !isPrinting }">
        <div class="mt-12 mb-12">
          <h1>小学生口算题</h1>
          <h3>姓名：__________ 日期：____月____日 时间：________ 对题：____道</h3>
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
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+5=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+10=</p>
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
          </div>
        </div>
      </div>
      <!-- 模拟第二份 -->
      <div class="sheet padding-10mm" :class="{ 'sheet-shadow': !isPrinting }">
        <div class="mt-12 mb-12">
          <h1>小学生口算题</h1>
          <h3>姓名：__________ 日期：____月____日 时间：________ 对题：____道</h3>
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
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+5=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+1=</p>
            <p>43+10=</p>
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
          </div>
        </div>
      </div>
      <div class="btn" v-if="!isPrinting">
        <ElButton class="mr-2 w-32" type="primary" @click="print">打印</ElButton>
      </div>
    </div>
  </div>
</template>

<script setup>
import { nextTick, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useAppStore } from "@/stores/app";


/**
 * 要处理的场景
 * 场景1: 一份试卷一页能显示完
 * 场景2: 一份试卷一页能不能显示完(A4纸一列最多26道题)
 * 场景3: 多份试卷一页能显示完
 * 场景4: 多份试卷一页能不能显示完
*/
const isPrinting = ref(false)
const route = useRoute()
const appStore = useAppStore()
onMounted(() => {
  console.log(appStore.printPreviewPapers)

  window.onbeforeprint = () => {
    console.log('before')
    isPrinting.value = true
  }

  window.onafterprint = () => {
    console.log('after')
    nextTick(() => {
      isPrinting.value = false
    })
  }
})

const print = () => {
  isPrinting.value = true
  nextTick(() => {
    window.print()
  })
}
</script>

<style lang="scss" scoped>
.preview {
  background: #e0e0e0;
  padding: 5mm;
  display: flex;
  justify-content: center;
  // height: 100vh;
}

.A4 {
  text-align: center;
}

.sheet {
  margin: 0;
  overflow: hidden;
  position: relative;
  box-sizing: border-box;
  page-break-after: always;
}

.sheet-shadow {
  box-shadow: 0 .5mm 2mm rgba(0, 0, 0, .3);
}

.A4 {
  .sheet {
    width: 210mm;
    // height: 296mm;
    background: white;

    @apply mt-2;

    &:first-of-type {
      @apply mt-0;
    }

    &.padding-10mm {
      padding: 10mm
    }

    &.padding-15mm {
      padding: 15mm
    }

    &.padding-20mm {
      padding: 20mm
    }

    &.padding-25mm {
      padding: 25mm
    }
  }
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
}

h1 {
  @apply text-3xl font-bold mb-5;
}

h3 {
  @apply text-base;
}

p {
  @apply text-sm;
  margin-right: 20%;
  margin-bottom: 16px;
}

.btn {
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 100;
  height: 50px;
  @apply flex justify-end items-center;
  @apply bg-black bg-opacity-50 w-full;
}
</style>