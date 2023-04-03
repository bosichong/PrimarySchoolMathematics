<template>
  <el-container>
    <el-aside width="150px">
      <Menu></Menu>
    </el-aside>
    <el-container>
      <el-header height="64px">
        <Header />
      </el-header>
      <el-main>
        <router-view />
      </el-main>
      <el-footer>
        <Footer />
      </el-footer>
    </el-container>
  </el-container>
</template>

<script setup>
import { Header, Footer, Menu } from "@/components";
</script>