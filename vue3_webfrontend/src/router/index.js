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
        component: () => import('../views/Print.vue'),
    }
];


export const router = createRouter({
    history: createWebHistory(),
    routes,
});