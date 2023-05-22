import { createRouter, createWebHistory } from 'vue-router'

export const routes = [
    {
        path: '/',
        redirect: '/home'
    },
    {
        path: '/home',
        name: 'home',
        component: () => import('../views/Layout.vue'),
    },
    {
        path: '/print',
        name: 'print',
        props: true,
        component: () => import('../views/Print.vue'),
    }
];


const baseUrl = import.meta.env.BASE_URL
// console.log(baseUrl)
export const router = createRouter({
    history: createWebHistory(baseUrl),
    // history: createWebHashHistory(),
    routes,
});