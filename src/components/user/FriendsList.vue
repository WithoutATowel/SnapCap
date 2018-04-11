<template>
  <div>
    <h5>{{ user_first }}'s Friends</h5>
    <div v-for='friend in friends'>
      <Friend class='friend' :friend='friend' />
    </div>
  </div>
</template>

<script>

import Friend from './Friend.vue'
import axios from 'axios'

export default {
  mounted () {
    this.getFriendsList()
  },
  props: ['user_first', 'id'],
  components: {
    Friend
  },
  data () {
    return {
      friends: []
    }
  },
  methods: {
    getFriendsList: function () {
      axios.get(`/api/api/user/${this.id}/friends/`)
        .then((response) => {
          this.friends = response.data
          // console.log('here is friendslist comp response.data: ', response.data)
        })
    }
  }
}
</script>

<style scoped>

.friend {
  margin: 1em 0;
}

</style>
