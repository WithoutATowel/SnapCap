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
import Toasted from 'vue-toasted';

Vue.use(Toasted)
//
// // you can also pass options, check options reference below
// Vue.use(Toasted, Options)

Vue.use(Vuex)
Vue.use(VueAxios, axios)
Vue.use(VModal, { dialog: true })

const store = new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    user: localStorage.getItem('u'),
    endpoints: {
      // heroku
      obtainJWT: 'https://snapcap-app.herokuapp.com/auth/obtain_token/',
      refreshJWT: 'https://snapcap-app.herokuapp.com/auth/refresh_token/'
      // obtainJWT: 'http://localhost:8000/auth/obtain_token/',
      // refreshJWT: 'http://localhost:8000/auth/refresh_token/'
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
          Vue.toasted.show('Logged In', {
             theme: "primary",
             position: "top-right",
             duration : 3000
          })
        })
        .catch((err) => {
          console.log(err.response)
          if (err.response.data.non_field_errors[0] === 'Unable to log in with provided credentials.') {
            Vue.toasted.error('Your username and password don\'t match', {
               theme: "primary",
               position: "top-right",
               duration : 3000
            })
          } else {
            Vue.toasted.error(err.response.data, {
               theme: "primary",
               position: "top-right",
               duration : 3000
            })
          }
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
      Vue.toasted.show('Logged Out', {
         theme: "primary",
         position: "top-right",
         duration : 3000
      })
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
