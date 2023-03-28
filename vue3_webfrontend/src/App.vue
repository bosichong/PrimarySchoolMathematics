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
  <!-- <a-layout>
    <a-layout-sider breakpoint="md" collapsed-width="0" @collapse="onCollapse" @breakpoint="onBreakpoint">
      <a-menu v-model:selectedKeys="selectedKeys" mode="inline">
        <a-menu-item key="1">
          <router-link to="/">
            <reload-outlined spin />
            <span class="nav-text">自由配置口算题</span>
          </router-link>

        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="/about">
            <check-outlined />
            <span class="nav-text">快速生成口算题</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <router-link to="/show">
          <user-outlined />
          <span class="nav-text">下载口算题</span>
        </router-link>
        </a-menu-item>
        <a-menu-item key="4">
          <router-link to="/about">
          <user-outlined />
          <span class="nav-text">About</span>
        </router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header :style="{ background: '#fff', padding: 0 }">
        <AppHeader />
      </a-layout-header>
      <router-view></router-view>
      <a-layout-footer style="text-align: center">
        <FooterVue />
      </a-layout-footer>
    </a-layout>
  </a-layout> -->
</template>

<script setup>
import { ref } from 'vue';
import { Header, Footer, Menu } from "@/components";

const onCollapse = (collapsed, type) => {
  // console.log(collapsed, type);
}
const onBreakpoint = broken => {
  // console.log(broken);
}

const selectedKeys = ref(['1'])

</script>