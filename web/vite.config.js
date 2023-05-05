import path from "path";
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const srcPath = path.resolve(__dirname, 'src')

export default defineConfig({
  server: {
    port: 1101,
  },
  resolve: {
    alias: {
      '@/': `${srcPath}/`,
    }
  },
  plugins: [vue()]
})
