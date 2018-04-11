<template>
  <div class='profile-page'>
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
        <p>{{ this.totalSnapVotes }}</p>
        <h4>Cap Points</h4>
        <p>{{ this.totalCapVotes }}</p>
      </div>
    </div>  <!-- END Top Profile Row -->
    <div class='row'>  <!-- Bottom Profile Row -->
      <div class='col s4'>
        <FriendsList v-if='user' :id='user.id' :user_first='user.first_name' />
      </div>
      <div class='col s4'>
        <SnapsList v-if='user' :snaps='user.picture_set' :user_first='user.first_name' />
      </div>
      <div class='col s4'>
        <CapsList v-if='user' :id='user.id' :user_first='user.first_name' />
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
      user: null,
      totalSnapVotes: 0,
      totalCapVotes: 0
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
          console.log('here is this.user.usercap_set: ', this.user.usercap_set)
          this.getTotalVotes()
        })
    },
    getTotalVotes: function () {
      this.user.usercap_set.forEach(cap => {
        this.totalCapVotes += cap.votes
      })
      this.user.picture_set.forEach(snap => {
        this.totalSnapVotes += snap.votes
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

.profile-page {
  padding: 1em;
  background-color: rgba(38, 232, 156, .4);
}

</style>
