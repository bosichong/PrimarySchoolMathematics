import { defineStore } from "pinia";

export const useAppStore = defineStore('app', {
  state: () => ({
    printPreviewPapers: []
  }),
  actions: {
    navigateToPrint(router, printPreviewPapers) {
      this.$patch((s) => {
        s.printPreviewPapers = printPreviewPapers
        router.push('/print')
      })
    }
  }
})