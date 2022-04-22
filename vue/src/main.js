import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { Icon } from '@iconify/vue';

import App from './App.vue'
import router from './router'
import './index.scss'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use({Icon})
app.use(router)

app.mount('#app')
