<template>
    <footer>
        <img alt="python-3.8.8" src="https://img.shields.io/badge/Python-3.8.8-green?logo=python" />
        <img alt="fastAPI-0.85.1" src="https://img.shields.io/badge/fastAPI-0.85.1-green" />
        <img alt="Vue-3.2.41" src="https://img.shields.io/badge/Vue-3.2.41-blue" />
        <img alt="Ant Design of Vue" src="https://img.shields.io/badge/Ant Design of Vue-3.2.14-blue" />
        <img alt="license-Apache--2.0" src="https://img.shields.io/badge/license-Apache--2.0-green" />
        <a href="https://gitee.com/J_Sky/PrimarySchoolMathematics" color="inherit">
            <img alt="" src="https://img.shields.io/badge/Gitee--PrimarySchoolMathematics-red?logo=gitee" />
        </a>
        <a href="https://github.com/bosichong/PrimarySchoolMathematics" color="inherit">
            <img alt="" src="https://img.shields.io/badge/Github--PrimarySchoolMathematics-green?logo=github" />
        </a>
    </footer>
</template>

<script setup>

</script>

<style lang="scss" scoped>
footer {
    padding: 25px 30px;
    color: #000000d9;
    font-size: 14px;
    background: #f0f2f5;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    align-items: baseline;

    img {
        margin-right: 6px;
    }

    a {
        margin-right: 6px;

        img {
            margin-right: 0;
        }
    }
}
</style>