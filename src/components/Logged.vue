<template>
  <div>
    <p><a class="modal-trigger" href="#login">Login</a>/<a class="modal-trigger" href="#signup">Signup</a> | {{ user }}</p>

    <!-- Modal Structure -->
    <div id="login" class="modal">
      <form>
        <div class="modal-content">
          <input type="text" placeholder="Email" />
          <input type="password" placeholder="Password" />
        </div>
        <div class="modal-footer">
          <button type="submit" class="modal-action modal-close waves-effect waves-green btn-flat">Login</button>
        </div>
      </form>
    </div>

    <div id="signup" class="modal">
      <form v-on:submit.prevent="onSubmit">
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
      }
    }
  },
  methods: {
    onSubmit (e) {
      e.preventDefault()
      // upload data to the server
      console.log(this.signup)
      axios.post('/api/api/users/', this.signup).then(result => {
        console.log(result.data)
      }).catch(err => {
        console.log(err)
      })
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
