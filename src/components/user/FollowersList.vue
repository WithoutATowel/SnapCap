<template>
  <div>
    <h5>{{ username }}'s Followers</h5>
    <div v-for='friend in friends'>
      <Follower class='friend' :friend='friend' />
    </div>
  </div>
</template>

<script>

import Follower from './Follower.vue'
import axios from 'axios'

export default {
  mounted () {
    this.getFriendsList()
  },
  props: ['username', 'id', 'getUser'],
  components: {
    Follower
  },
  data () {
    return {
      friends: []
    }
  },
  methods: {
    getFriendsList: function () {
      axios.get(`/api/api/user/${this.$route.params.id}/friends/`)
        .then((response) => {
          this.friends = response.data
          console.log('here is friends', response.data)
        })
    }
  },
  watch: {
    '$route' (to, from) {
      if (from !== to) {
        this.getFriendsList()
      }
    }
  }
}
</script>

<style scoped>

.friend {
  margin: 1em 0;
}

</style>
