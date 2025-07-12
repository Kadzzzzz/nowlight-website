import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LanguageSelection from './views/LanguageSelection.vue'
import Home from './views/Home.vue'
import './style.css'

const routes = [
  {
    path: '/',
    name: 'LanguageSelection',
    component: LanguageSelection,
    beforeEnter: (to, from, next) => {
      // Vérifier si une langue est déjà sélectionnée
      const savedLang = localStorage.getItem('nowlight-language')
      if (savedLang) {
        next('/home')
      } else {
        next()
      }
    }
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    } else {
      return { top: 0 }
    }
  }
})

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)
app.mount('#app')