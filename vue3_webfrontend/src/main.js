/*
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-15 08:18:31
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-12-01 23:10:32
 * @FilePath: /PrimarySchoolMath/vue3_webfrontend/src/main.js
 */
import { createApp } from 'vue'
import Antd from 'ant-design-vue';
import App from './App.vue'
import 'ant-design-vue/dist/antd.css';
import router from './router';
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'
const app = createApp(App);
app.use(Antd);
app.use(router)
app.mount('#app');
