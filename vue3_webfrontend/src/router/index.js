/*
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-15 08:18:31
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-12-01 23:24:16
 * @FilePath: /PrimarySchoolMath/vue3_webfrontend/src/router/index.js
 */
import { createRouter,createWebHistory } from 'vue-router'

import Home from '../components/Home.vue'
import About from '../components/About.vue'
import Show from '../components/Show.vue'

const routes =[
    {
        path:'/',
        name:'home',
        component:Home
    },
    {
        path:'/show',
        name:'show',
        component:Show
    },
    {
        path:'/about',
        name:'about',
        component:About,
    },
];


const router = createRouter({
    history:createWebHistory(),
    routes,
});

export default router