import { createRouter, createWebHistory } from 'vue-router'
import home from '../components/Home.vue'
import summoner from '../components/Summoner.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: home,
    },
    {
      path: '/summoner/:id',
      component: summoner,
    }
  ]
})

export default router