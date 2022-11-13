import { createRouter,createWebHistory } from 'vue-router'

import Home from '../components/Home.vue'
import About from '../components/About.vue'

const routes =[
    {
        path:'/',
        name:'home',
        component:Home
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