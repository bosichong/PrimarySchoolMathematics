<template>
    <footer class="py-6 px-7 flex justify-center flex-wrap items-baseline">
        <template v-for="bind in bands">
            <p class="h-7">
                <a v-if="bind.link" :href="bind.link" target="_blank">
                    <img :alt="bind.imageAlt" :src="bind.imageSrc" class="mr-2" />
                </a>
                <img v-else :alt="bind.imageAlt" :src="bind.imageSrc" class="mr-2" />
            </p>
        </template>
    </footer>
</template>

<script setup>
import { ref } from 'vue';

const bands = ref([
    { imageAlt: "python-3.8.8", imageSrc: "https://img.shields.io/badge/Python-3.8.8-green?logo=python" },
    { imageAlt: "fastAPI-0.85.1", imageSrc: "https://img.shields.io/badge/fastAPI-0.85.1-green" },
    { imageAlt: "Vue-3.2.41", imageSrc: "https://img.shields.io/badge/Vue-3.2.41-blue" },
    { imageAlt: "license-Apache--2.0", imageSrc: "https://img.shields.io/badge/license-Apache--2.0-green" },
    { imageAlt: "", imageSrc: "https://img.shields.io/badge/Gitee--PrimarySchoolMathematics-red?logo=gitee", link: 'https://gitee.com/J_Sky/PrimarySchoolMathematics' },
    { imageAlt: "", imageSrc: "https://img.shields.io/badge/Github--PrimarySchoolMathematics-green?logo=github", link: 'https://github.com/bosichong/PrimarySchoolMathematics' }
])
</script>

<style lang="scss" scoped>
footer {
    background: #f0f2f5;
}
</style>