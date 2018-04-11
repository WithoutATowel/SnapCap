<template>
  <div>
    <div class='row'>  <!-- Top Profile Row -->
      <div class='col s5'>  <!-- Pic Col Row -->
        <div class='row'>  <!-- Pic Row -->
          <div class='col s12'>
            <span>pic</span>
          </div>
        </div>
        <div class='row'>  <!-- Edit Profile Component Row -->
          <div class='col s12'>
            <EditProfile />
          </div>
        </div>
      </div>
      <div class='col s7'>
        <!-- <h2 v-if='user' >{{ firstName() }} {{ user.last_name }}</h2> -->
        <h2 v-if='user' >{{ user.first_name }} {{ user.last_name }}</h2>
        <h4>Snap Points</h4>
        <p># of Points</p>
        <h4>Cap Points</h4>
        <p># of Points</p>
      </div>
    </div>  <!-- END Top Profile Row -->
    <div class='row'>  <!-- Bottom Profile Row -->
      <div class='col s4'>
        <FriendsList v-if='user' :friends='user.friends' :user_first='user.first_name' />
      </div>
      <div class='col s4'>
        <SnapsList v-if='user' :snaps='user.picture_set' :user_first='user.first_name' />
      </div>
      <div class='col s4'>
        <CapsList v-if='user' :usercaps='user.usercap_set' :user_first='user.first_name' />
      </div>
    </div>  <!-- END Bottom Profile Row -->
  </div>
</template>

<script>

import EditProfile from './user/EditProfile'
import FriendsList from './user/FriendsList'
import SnapsList from './user/SnapsList'
import CapsList from './user/CapsList'
import axios from 'axios'

export default {
  mounted () {
    this.getUser()
  },
  props: ['id'],
  components: {
    EditProfile,
    FriendsList,
    SnapsList,
    CapsList
  },
  data () {
    return {
      user: null
    }
  },
  methods: {
    getUser: function () {
      console.log('clicked on getUser', this.id)
      axios.get(`/api/api/users/${this.id}/`)
        .then((response) => {
          this.user = response.data
          console.log('here is profile page response.data: ', response.data)
          console.log('here is profile page friends: ', response.data.friends)
          console.log('here is profile page picture_set: ', response.data.picture_set)
          console.log('here is profile page usercaps_set: ', response.data.usercaps_set)
        })
    }
    // firstName: function () {
    //   if (user)  {
    //     return user.first_name
    //   } else {
    //     return ''
    //   }
    // }
  }
}
</script>

<style scoped>

span {
  display: inline-block;
  height: 15em;
  width: 15em;
  background: lightblue;
}

.row {
  background: lightgrey;
}

.col {
  background: darkgrey;
}

</style>
