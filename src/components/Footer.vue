<template>
  <footer class="py-6 px-7 flex justify-center flex-wrap items-baseline">
    <template v-for="bind in bands">
      <p class="h-7">
        <a v-if="bind.link" :href="bind.link" target="_blank">
          <img :alt="bind.imageAlt" :src="bind.imageSrc" class="mr-2"/>
        </a>
        <img v-else :alt="bind.imageAlt" :src="bind.imageSrc" class="mr-2"/>
      </p>
    </template>

    <el-tooltip
        class="box-item"
        content="请作者喝一杯咖啡！"
        placement="top"
    >
      <el-button type="success" :icon="Coffee" size="large" circle @click="centerDialogVisible = true" class="fixed right-5 inset-y-1/4 text-lg"/>
    </el-tooltip>

    <el-dialog v-model="centerDialogVisible" title="请作者喝一杯咖啡：）" width="30%" center>
      <el-row :gutter="20">
        <el-col :span="12">
          <div class="grid-content ep-bg-purple"/>
          <img src="@/assets/wx.png" alt="请作者喝咖啡：）"></el-col>
        <el-col :span="12">
          <div class="grid-content ep-bg-purple"/>
          <img src="@/assets/zfb.png" alt="请作者喝咖啡：）"></el-col>
      </el-row>
      <div>


      </div>
    </el-dialog>

  </footer>
</template>

<script setup>
import {ref} from 'vue';
import {
  Coffee,
} from '@element-plus/icons-vue'

const centerDialogVisible = ref(false)


const bands = ref([
  {imageAlt: "Vue-3.2.41", imageSrc: "https://img.shields.io/badge/Vue-3.2.41-blue"},
  {imageAlt: "license-Apache--2.0", imageSrc: "https://img.shields.io/badge/license-Apache--2.0-green"},
  {
    imageAlt: "",
    imageSrc: "https://img.shields.io/badge/Gitee--PrimarySchoolMathematics-red?logo=gitee",
    link: 'https://gitee.com/J_Sky/PrimarySchoolMathematics'
  },
  {
    imageAlt: "",
    imageSrc: "https://img.shields.io/badge/Github--PrimarySchoolMathematics-green?logo=github",
    link: 'https://github.com/bosichong/PrimarySchoolMathematics'
  }
])
</script>

<style lang="scss" scoped>
footer {
  background: #f0f2f5;
}
</style>