<template>
  <div :class="{ 'preview': !isPrinting }">
    <div class="A4">
      <div class="sheet padding-10mm">
        <div class="mb-12">
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

const isPrinting = ref(false)
onMounted(() => {
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
  // position: relative;
}

.sheet {
  margin: 0;
  overflow: hidden;
  position: relative;
  box-sizing: border-box;
  page-break-after: always;
}

.A4 {
  .sheet {
    width: 210mm;
    height: 296mm;
    background: white;
    box-shadow: 0 .5mm 2mm rgba(0, 0, 0, .3);

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
  @apply text-3xl font-bold mb-4;
}

h3 {
  @apply text-lg;
}

p {
  @apply text-base;
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