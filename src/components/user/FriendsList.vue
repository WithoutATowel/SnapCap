<template>
  <div>
    <h5>{{ user_first }}'s Friends</h5>
    <!-- <div v-for='friend in friends'>
      <Friend :friend='friend' />
    </div> -->
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
      data: 'NO DATA'
    }
  },
  methods: {
    getFriendsList: function () {
      axios.get(`/api/api/user/${this.id}/friends/`)
        .then((response) => {
          this.user = response.data
          console.log('here is friendslist comp response.data: ', response.data)
        })
    }
  }
}
</script>

<style scoped>



</style>
