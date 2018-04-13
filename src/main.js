// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Nav from './components/Nav'
import Footer from './components/Footer'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwtDecode from 'jwt-decode'
import Vuex from 'vuex'
import VModal from 'vue-js-modal'

Vue.use(Vuex)
Vue.use(VueAxios, axios)
Vue.use(VModal, { dialog: true })

const store = new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    user: localStorage.getItem('u'),
    endpoints: {
      obtainJWT: 'http://localhost:8000/api/auth/obtain_token/',
      refreshJWT: 'http://localhost:8000/api/auth/refresh_token/'
    }
  },
  mutations: {
    updateToken (state, newToken) {
      localStorage.setItem('t', newToken.token)
      localStorage.setItem('u', JSON.stringify(newToken.user))
      state.jwt = newToken.token
      state.user = newToken.user
    },
    removeToken (state) {
      localStorage.removeItem('t')
      localStorage.removeItem('u')
      state.jwt = null
      state.user = null
    }
  },
  actions: {
    obtainToken (context, usernamePass) {
      const payload = {
        'username': usernamePass[0],
        'password': usernamePass[1]
      }
      axios.post(this.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.commit('updateToken', {token: response.data.token, user: response.data.user})
        })
        .catch((error) => {
          console.log(error)
        })
    },
    refreshToken () {
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response) => {
          this.commit('updateToken', {token: response.data.token, user: response.data.user})
        })
        .catch((error) => {
          console.log(error)
        })
    },
    inspectToken () {
      const token = this.state.jwt
      if (token) {
        const decoded = jwtDecode(token)
        const exp = decoded.exp
        const origIat = decoded.origIat
        if (exp - (Date.now() / 1000) < 1800 && (Date.now() / 1000) - origIat < 628200) {
          this.dispatch('refreshToken')
        } else if (exp - (Date.now() / 1000) < 1800) {
          // DO NOTHING, DO NOT REFRESH
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    },
    logout () {
      this.commit('removeToken')
    }
  }
})

Vue.config.productionTip = false

Vue.component('Nav', Nav)
Vue.component('Footer', Footer)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
