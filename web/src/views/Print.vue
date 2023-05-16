<template>
  <div :class="{ 'preview': !isPrinting }">
    <div class="A4">
      <div v-for="sheet in sheets" class="sheet padding-10mm" :class="{ 'sheet-shadow': !isPrinting }">
        <div class="mt-12 mb-12">
          <h1>{{ sheet.paperTitle }}</h1>
          <h3>{{ sheet.paperSubTitle }}</h3>
        </div>
        <div class="row">
          <div v-for="col in sheet.columnsOfPaper" :style="`width: ${sheet.colWidth}%;`">
            <p :style="`margin-bottom: ${sheet.rowHeight}`" v-for="f in col">{{ f }}</p>
          </div>
        </div>
      </div>
      <div class="btn" v-if="!isPrinting">
        <ElButton @click="goBack">返回</ElButton>
        <ElButton class="mr-2 w-32" type="primary" @click="print">打印</ElButton>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, nextTick, onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
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
const router = useRouter()
const appStore = useAppStore()

const sheets = computed(() => {
  return appStore.printPreviewPapers.map(p => {
    const { paperTitle, paperSubTitle, numberOfPagerColumns, solution, formulas } = p

    const numberOfCols = formulas.length / numberOfPagerColumns
    const colWidth = 100 / numberOfPagerColumns
    const rowHeight = solution == '0' ? '16px' : '160px'

    let columnsOfPaper = [];
    let index = 0
    while (index < formulas.length) {
      columnsOfPaper.push(formulas.slice(index, numberOfCols + index));
      index += numberOfCols;
    }
    columnsOfPaper = columnsOfPaper.reverse()
    console.log(columnsOfPaper);
    return { paperTitle, paperSubTitle, columnsOfPaper, colWidth, rowHeight }
  })
})

onMounted(() => {
  // 修改网页标题以作为打印时文件的文件名
  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth() + 1;
  const day = now.getDate();
  const hour = now.getHours();
  const minute = now.getMinutes();
  const second = now.getSeconds();
  const timeStr = `${year}${month}${day}${hour}${minute}${second}`;
  console.log(timeStr);
  document.title = route.query.fileName + timeStr

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

const goBack = () => {
  router.back()
}

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