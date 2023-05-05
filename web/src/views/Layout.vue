<template>
  <el-container>
    <el-header height="64px">
      <Header />
    </el-header>
    <el-main>
      <Home />
    </el-main>
    <el-footer>
      <Footer />
    </el-footer>
  </el-container>
</template>

<script setup>
import { Header, Footer, Menu } from "@/components";
import Home from "./Home.vue";
</script>

<style lang="scss" scoped></style>