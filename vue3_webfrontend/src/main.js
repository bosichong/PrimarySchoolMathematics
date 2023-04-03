/*
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-15 08:18:31
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-12-01 23:10:32
 * @FilePath: /PrimarySchoolMath/vue3_webfrontend/src/main.js
 */
import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router';
import "./styles/shared.scss";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(ElementPlus)
app.use(router)
app.mount('#app');
