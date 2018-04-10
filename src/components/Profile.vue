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
        <h2>User Name here #{{ id }}</h2>
        <h4>Snap Points</h4>
        <p># of Points</p>
        <h4>Cap Points</h4>
        <p># of Points</p>
      </div>
    </div>  <!-- END Top Profile Row -->
    <div class='row'>  <!-- Bottom Profile Row -->
      <div class='col s4'>
        <FriendsList />
      </div>
      <div class='col s4'>
        <SnapsList />
      </div>
      <div class='col s4'>
        <CapsList />
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
          this.snaps = response.data
          console.log(response.data)
        })
    }
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
