import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import SnapShow from '@/components/SnapShow'
import Profile from '@/components/Profile'

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
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    }
  ]
})
