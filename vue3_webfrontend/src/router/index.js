/*
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-15 08:18:31
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-12-01 23:24:16
 * @FilePath: /PrimarySchoolMath/vue3_webfrontend/src/router/index.js
 */
import { createRouter, createWebHistory } from 'vue-router'

export const routes = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        name: 'home',
        component: () => import('../views/Home.vue'),
    }
];


export const router = createRouter({
    history: createWebHistory(),
    routes,
});