import path from "path";
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { createHtmlPlugin } from "vite-plugin-html";

const srcPath = path.resolve(__dirname, 'src')

export default defineConfig({
  base: '/PrimarySchoolMathematics',
  server: {
    port: 1101,
  },
  resolve: {
    alias: {
      '@/': `${srcPath}/`,
    }
  },
  plugins: [
    vue(),
    createHtmlPlugin({
      inject: {
        data: {
          title: '小学数学口算题 | Primary School Mathematics'
        }
      }
    })
  ]
})
