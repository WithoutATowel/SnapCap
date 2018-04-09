import Vue from 'vue'
import Router from 'vue-router'
import Goodbye from '@/components/Goodbye'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Goodbye
    }
  ]
})
