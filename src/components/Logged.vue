<template>
  <div>

    <p v-if="!$store.state.user"><a class="modal-trigger" href="#login">Login</a>/<a class="modal-trigger" href="#signup">Signup</a></p>
    <div v-if="$store.state.user"><a v-on:click="logout" href="#">Logout</a> | {{ $store.state.user.username }}</div>
    <!-- Modal Structure -->
    <div id="login" class="modal">
      <form v-on:submit.prevent="onLoginSubmit">
        <div class="modal-content">
          <input type="text" v-model="login['username']" placeholder="Username" />
          <input type="password" v-model="login['password']" placeholder="Password" />
        </div>
        <div class="modal-footer">
          <button type="submit" class="modal-action modal-close waves-effect waves-green btn-flat">Login</button>
        </div>
      </form>
    </div>

    <div id="signup" class="modal">
      <form v-on:submit.prevent="onSignupSubmit">
        <div class="modal-content">

          <input type="text" name="first-name" v-model="signup['first_name']" placeholder="First Name"/>
          <input type="text" name="last-name" v-model="signup['last_name']" placeholder="Last Name"/>
          <input type="text" name="username" v-model="signup['username']" placeholder="Username" />
          <input type="text" name="email" v-model="signup['email']" placeholder="Email" />
          <input type="password" name="password" v-model="signup['password']" placeholder="Password" />
        </div>
        <div class="modal-footer">
          <button type="submit" class="modal-action modal-close waves-effect waves-green btn-flat">Sign Up</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      user: 'NO USER',
      signup: {
        'username': '',
        'first_name': '',
        'last_name': '',
        'email': '',
        'password': ''
      },
      login: {
        'username': '',
        'password': ''
      }
    }
  },
  methods: {
    onSignupSubmit (e) {
      e.preventDefault()
      // upload data to the server
      console.log(this.signup)
      axios.post('/api/api/users/', this.signup).then(result => {
        console.log(result.data)
      }).catch(err => {
        console.log(err)
      })
    },
    ...mapActions([
      'obtainToken'
    ]),
    onLoginSubmit (e) {
      e.preventDefault()
      //console.log('onLoginSubmit fired')
      this.$store.dispatch('obtainToken', [this.login.username, this.login.password])
      // console.log(this.login)
      // axios.get('/api/api/users/', this.signup).then(result => {
      //   console.log(result.data)
      // }).catch(err => {
      //   console.log(err)
      // })
    },
    logout () {
      this.$store.dispatch('logout')
    }

  }
}
</script>

<style scoped>
  h2 {
    color: red
  }
  p {
    margin: 0px;
  }
</style>
