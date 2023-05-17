import { createApp } from 'vue'
import { createPinia } from "pinia"
import App from './App.vue'
import { router } from './router';
import ElementPlus from 'element-plus'
import "./styles/tailwind.css";
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import "./styles/shared.scss";

import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const pinia = createPinia()
const app = createApp(App);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(pinia)
app.use(ElementPlus, {
  locale: zhCn,
})
app.use(router)
app.mount('#app');
