<template>
  <a-layout>
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
  </a-layout>


</template>
<script setup>
import { UserOutlined, CheckOutlined, ReloadOutlined } from '@ant-design/icons-vue';
import { ref } from 'vue';
import AppHeader from './components/AppHeader.vue';
import FooterVue from './components/Footer.vue';


const onCollapse = (collapsed, type) => {
  // console.log(collapsed, type);
}
const onBreakpoint = broken => {
  // console.log(broken);
}

const selectedKeys = ref(['1'])

</script>
<style>
.ant-layout{
  height: auto;
}
.ant-layout-content{
  max-width: 750px;
}
.ant-layout.ant-layout-has-sider > .ant-layout{
  background:#fff;
  
}

.ant-menu-root.ant-menu-inline{
  height: 100%;
}
.ant-layout .ant-layout-sider{
  background: #fff;
  height: auto;
}


.site-layout-sub-header-background {
  background: #fff;
}

.site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout-sub-header-background {
  background: #141414;
}

.ant-layout-sider .ant-layout-sider-zero-width-trigger  {
  background:#52c41a;
  top:80px;
  height: 36px;
  line-height: 36px;
}


#app {
  width: 100%;
  height: 100%;
}

.ant-layout {
  height: auto;
}
</style>