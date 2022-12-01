<!--
 * @Author: J.sky bosichong@qq.com
 * @Date: 2022-11-15 12:32:07
 * @LastEditors: J.sky bosichong@qq.com
 * @LastEditTime: 2022-12-01 23:49:54
 * @FilePath: /PrimarySchoolMath/vue3_webfrontend/src/components/Show.vue
-->
<template lang="">
    <a-layout-content :style="{ margin: '24px 16px 0',height:'100% '}">
      <div :style="{ padding: '24px', background: '#fff', height: '100%' }">
        <a-typography-title :level="3">口算题文件下载</a-typography-title>
      

<a-row v-if="psmlist.length">
  <a-col :span="6"><a v-bind:href="psmzip" target="_blank" download="下载">所有口算题打包zip下载</a></a-col>
    <a-col  v-for="item of psmlist" :span="6"><a v-bind:href="psmlink + item" target="_blank" download="下载">{{ item }}</a></a-col>
</a-row>
<p v-else>还没有生成口算题的卷子哦,请先生成口算题再回到这里下载.</p>


      
     
      

      
      </div>
    </a-layout-content>
</template>
<script setup>
import {ref} from 'vue'
import axios from 'axios'
const psmlist = ref('')
const psmlink = ref('dist/docx/')
const psmzip = ref('dist/docx/docs.zip')

axios.get('getpsmlist').then(function (res) {
    
    psmlist.value = res.data
})

</script>
<style lang="">
    
</style>