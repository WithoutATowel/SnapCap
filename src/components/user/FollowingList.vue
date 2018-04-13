<template>
  <div>
    <h5>{{ username }} is following</h5>
    <div v-for='friend in friends'>
      <Following class='friend' :friend='friend' />
    </div>
  </div>
</template>

<script>

import Following from './Following.vue'
import axios from 'axios'

export default {
  mounted () {
    this.getFriendsList()
  },
  props: ['username', 'id', 'getUser'],
  components: {
    Following
  },
  data () {
    return {
      friends: []
    }
  },
  methods: {
    getFriendsList: function () {
      axios.get(`/api/user/${this.$route.params.id}/friends/`)
        .then((response) => {
          this.friends = response.data
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
