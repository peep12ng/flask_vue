import { createRouter, createWebHistory } from 'vue-router'
import Test from '../components/Test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/test',
      name: 'test',
      component: Test
    }
  ]
})

export default router