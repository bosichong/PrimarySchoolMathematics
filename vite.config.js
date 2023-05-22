import path from "path";
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {createHtmlPlugin} from "vite-plugin-html";
import {viteStaticCopy} from "vite-plugin-static-copy";

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
    plugins: [
        vue(),
        createHtmlPlugin({
            inject: {
                data: {
                    title: '小学数学口算题 | Primary School Mathematics'
                }
            }
        }),
        viteStaticCopy({
            silent: true,
            targets: [
                {
                    src: 'dist/*',
                    dest: path.resolve(__dirname, 'docs')
                }
            ]
        })
    ],
    base:'./',
    build: {
        chunkSizeWarningLimit: 1500,
    },
})
