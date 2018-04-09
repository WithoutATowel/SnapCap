import Vue from 'vue'
import Router from 'vue-router'
import SnapShow from '@/components/SnapShow'
import Nav from '@/components/Nav'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/snaps',
      name: 'SnapShow',
      component: SnapShow
    }
  ]
})
