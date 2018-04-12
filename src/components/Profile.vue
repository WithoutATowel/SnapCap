<template>
  <div class='profile-page'>
    <div class='row'>  <!-- Top Profile Row -->
      <div class='col s5'>  <!-- Pic Col Row -->
        <div class='row'>  <!-- Pic Row -->
          <div class='col s12'>
            <img v-if="user !== null" v-bind:src="user.profile.profile_img" />
          </div>
        </div>
        <div class='row'>  <!-- Edit Profile Component Row -->
          <div class='col s12'>
            <UpdateProfileSection />
          </div>
        </div>
      </div>
      <div class='col s7'>
        <!-- <h2 v-if='user' >{{ firstName() }} {{ user.last_name }}</h2> -->
        <h2 v-if='user' >{{ user.username }}</h2>
        <button v-if='$store.state.user.id !== this.$route.params.id' v-on:click="toggleFollow">
          <span v-if='this.isFriend'>Unfollow</span>
          <span v-else>Follow</span>
        </button>
        <h4>Snap Points</h4>
        <p>{{ this.totalSnapVotes }}</p>
        <h4>Cap Points</h4>
        <p>{{ this.totalCapVotes }}</p>
      </div>
    </div>  <!-- END Top Profile Row -->
    <div class='row'>  <!-- Bottom Profile Row -->
      <div class='col s4'>
        <FriendsList v-if='user' v-bind='{ id: user.id, username: user.username, }' />
      </div>
      <div class='col s4'>
        <SnapsList v-if='user' :snaps='this.user.picture_set' :username='this.user.username' />
      </div>
      <div class='col s4'>
        <CapsList v-if='user' :id='this.user.id' :username='this.user.username' />
      </div>
    </div>  <!-- END Bottom Profile Row -->
  </div>
</template>

<script>

import UpdateProfileSection from './user/UpdateProfileSection'
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
    UpdateProfileSection,
    FriendsList,
    SnapsList,
    CapsList
  },
  data () {
    return {
      user: null,
      totalSnapVotes: 0,
      totalCapVotes: 0,
      isFriend: false
    }
  },
  methods: {
    getUser: function () {
      console.log('clicked on getUser', this.id)
      axios.get(`/api/api/users/${this.id}/`)
        .then((response) => {
          this.user = response.data
          console.log('here is profile page response.data: ', response.data)
          console.log('here is this.user.picture_set: ', this.user.picture_set)
          this.getTotalVotes()
          this.checkIsFriend()
        })
    },
    getTotalVotes: function () {
      this.totalCapVotes = 0
      this.user.usercap_set.forEach(cap => {
        this.totalCapVotes += cap.votes
      })
      this.totalSnapVotes = 0
      this.user.picture_set.forEach(snap => {
        this.totalSnapVotes += snap.votes
      })
    },
    checkIsFriend: function () {
      for (let friend of this.$store.state.user.friends) {
        if (friend.friend === parseInt(this.$route.params.id)) {
          this.isFriend = true
        }
      }
    },
    toggleFollow: function () {
      axios.post(`/api/api/friends/${this.$store.state.user.id}/${this.$route.params.id}/`, {}, {
        headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
      }).then( (response) => {
        this.$store.state.user = response.data
        localStorage.u = response.data
        this.isFriend = !this.isFriend 
      })
    },
  },
  watch: {
    '$route' (to, from) {
      if (from !== to) {
        this.getUser()
      }
    }
  }
}
</script>

<style scoped>

/*span {
  display: inline-block;
  height: 15em;
  width: 15em;
  background: lightblue;
}*/

.profile-page {
  padding: 1em;
  background-color: rgba(38, 232, 156, .4);
}

</style>
