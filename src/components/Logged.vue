<template>
  <div>
    <p v-if="!$store.state.user">
      <button v-on:click="show('login')" class="header-button">Login</button> or
      <button v-on:click="show('signup')" class="header-button">Signup</button></p>
    <div v-if="$store.state.user">
      <button v-on:click="logout" class="header-button">Logout</button> |
      <router-link :to="{ name: 'Profile', params: { id: $store.state.user.id } }">
        <p class='username'>{{ $store.state.user.username }}</p>
      </router-link>
    </div>

    <modal name="login">
      <div class="row-fluid">
        <div class="col s6">
          <div class="main-modal">
            <form v-on:submit.prevent="onLoginSubmit('login')">
              <div class="modal-content">
                <input type="text" v-model="login['username']" placeholder="Username" />
                <input type="password" v-model="login['password']" placeholder="Password" />
              </div>
              <div class="modal-footer">
                <button type="submit" class="yellow-btn btn-flat">Login</button>
              </div>
            </form>
          </div>
        </div>
        <div class="col s6 login-img-cont">
          <img src="/static/img/login.jpeg" />
        </div>
      </div>
    </modal>

    <modal name="signup" height="auto" :scrollable="true" :adaptive="true">
      <div class="row-fluid">
        <div class="col s6">
          <div class="main-modal">
            <form v-on:submit.prevent="onSignupSubmit('signup')">
              <div class="modal-content">
                <input type="text" name="first-name" v-model="signup['first_name']" placeholder="First Name"/>
                <input type="text" name="last-name" v-model="signup['last_name']" placeholder="Last Name"/>
                <input type="text" name="username" v-model="signup['username']" placeholder="Username" />
                <input type="text" name="email" v-model="signup['email']" placeholder="Email" />
                <input type="password" name="password" v-model="signup['password']" placeholder="Password" />
              </div>
              <div class="modal-footer">
                <button type="submit" class="yellow-btn btn-flat">Sign Up</button>
              </div>
            </form>
          </div>
        </div>
        <div class="col s6 signup-img-cont">
          <img src="/static/img/signup.jpeg" />
        </div>
      </div>
    </modal>
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
      },
      login: {
        'username': '',
        'password': ''
      }
    }
  },
  methods: {
    onSignupSubmit () {
      this.$modal.hide('signup')
      axios.post('/api/users/', this.signup).then(result => {
        this.$toasted.show('You Are Now Signed Up!', {
           theme: "primary",
           position: "top-right",
           duration : 3000
        })
        this.$store.dispatch('obtainToken', [result.data.username, this.signup.password])
        let profilePicUrl = 'https://www.avatarapi.com/js.aspx?email=' + result.data.email + '&size=200'
        axios.get(profilePicUrl).then(response => {
          var profilePic = response.data.match(/(https?:\/\/[^\s']+)/g) ? response.data.match(/(https?:\/\/[^\s']+)/g)[1] : null
          if (profilePic) {
            axios.put('/api/profile/' + result.data.profile.id + '/', {
              user: result.data.id,
              profile_img: profilePic
            }, {
              headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
            })
          } else {
            axios.put('/api/profile/' + result.data.profile.id + '/', {
              user: result.data.id,
              profile_img: 'http://www.everythingjustrocks.com/wp-content/uploads/default.png'
            }, {
              headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
            })
          }
        })
      }).catch(err => {
        console.log(err.response)
        this.$toasted.error('Oops, something went wrong!', {
           theme: "primary",
           position: "top-right",
           duration : 3000
        })
        if (err.response.data.non_field_errors[0] === 'That username already exists, bro') {
          this.$modal.show('dialog', {
            title: 'Alert!',
            text: 'That username already exists 😬',
            buttons: [
              {
                title: 'OK',
                default: true
              }
            ]
          })
        }
      })
    },
    onLoginSubmit (type) {
      this.$store.dispatch('obtainToken', [this.login.username, this.login.password])
      this.$modal.hide(type)
    },
    logout () {
      this.$store.dispatch('logout')
    },
    show (type) {
      this.$modal.show(type)
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
  .username {
    display: inline-block;
    font-size: 1.2rem;
    color: #fff;
  }
  .login-img-cont, .signup-img-cont {
    display: flex;
    justify-content: center;
    align-items: center;
    max-height: 100%;
    overflow: hidden;
  }
  .login-img-cont img {
    margin-left: -100px;
    margin-top: 0px;
    width: auto;
    height: 100%;
    max-width: initial;
  }
  .signup-img-cont img {
    width: auto;
    height: 100%;
    max-width: initial;
  }
  .row-fluid, .s6 {
    height: 100%;
  }
  .main-modal {
    height: 100%
  }

</style>
