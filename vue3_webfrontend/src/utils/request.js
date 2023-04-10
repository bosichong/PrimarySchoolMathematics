import axios from 'axios'
import { ElMessage } from 'element-plus'

const service = axios.create({
  baseURL: process.env.NODE_ENV == 'production' ? '/' : 'http://localhost:1101',
  timeout: 1000 * 10
})

// request拦截器
service.interceptors.request.use(
  (config) => {
    if (config.method === 'get') {
      const random = 't=' + Date.now()
      if (config.url.indexOf('?') > 0) {
        config.url += '&' + random
      } else {
        config.url += '?' + random
      }
    }

    console.debug(`Call API Url: ${config.url}`)

    return config
  },
  (error) => {
    console.error(error)
    Promise.reject(error)
  }
)

// response拦截器
service.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    const { response } = error
    showMessage(response.data?.detail)
    return Promise.reject(error)
  }
)

function showMessage(message) {
  ElMessage.error({
    message,
    duration: 1000 * 5
  })
}

export default service
