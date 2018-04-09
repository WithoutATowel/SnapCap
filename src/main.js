// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Nav from './components/Nav'
import Footer from './components/Footer'
import router from './router'

Vue.config.productionTip = false

Vue.component('Nav', Nav);
Vue.component('Footer', Footer);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
