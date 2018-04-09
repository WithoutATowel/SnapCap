import Vue from 'vue'
import Router from 'vue-router'
import Goodbye from '@/components/Goodbye'
import Hello from '@/components/Hello'
import Main from '@/components/Main'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/goodbye',
      name: 'Goodbye',
      component: Goodbye
    }
  ]
})
