<template>
  <el-dialog v-model="currentVisible" title="口算题文件下载" append-to-body :close-on-click-modal="false" @open="open" @closed="closed">
    <el-row :gutter="10">
      <el-col :span="12">
        <a :href="zipUrl" target="_blank" download="下载">所有口算题打包zip下载</a>
      </el-col>
      <el-col :span="12" v-for="file in files">
        <a :href="fileUrl + file" target="_blank" :download="file">{{ file }}</a>
      </el-col>
    </el-row>
    <template #footer>
      <el-button type="primary" @click="currentVisible = false">关闭</el-button>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, computed } from 'vue';
import { getDownloadLinksOfPapers } from '@/apis/paper';

const props = defineProps({
  visible: {
    type: Boolean
  },
})

const emit = defineEmits(['update:visible'])

const currentVisible = computed({
  get() {
    return props.visible
  },
  set(val) {
    emit('update:visible', val)
  }
})

const files = ref([])
const fileUrl = ref('dist/docx/')
const zipUrl = ref('dist/docx/docs.zip')
const open = async () => {
  // 调用接口获取试卷下载地址
  const { data } = await getDownloadLinksOfPapers()
  files.value = data
}

const closed = () => {

}
</script>

<style lang="scss" scoped></style>