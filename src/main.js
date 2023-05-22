import { createApp } from 'vue'
import { createPinia } from "pinia"
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import "./styles/tailwind.css";
import "./styles/shared.scss";
import 'element-plus/dist/index.css'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import App from './App.vue'
import { router } from './router';

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
