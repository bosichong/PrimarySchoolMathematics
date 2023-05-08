import { defineStore } from "pinia";

export const useAppStore = defineStore('app', {
  state: () => ({
    printPreviewPapers: []
  }),
  actions: {
    /**
     * 
     * @param {import("vue-router").Router} router 
     * @param {String} fileName 
     * @param {Array} printPreviewPapers 
     */
    navigateToPrint(router, fileName, printPreviewPapers) {
      this.$patch((s) => {
        s.printPreviewPapers = printPreviewPapers
        router.push({ path: '/print', query: { fileName } })
      })
    }
  }
})