<template>
  <div>
    <h2 v-for='friend in friends'>{{ friend }}</h2>
    <div v-for='snap in topSnaps'>
      <FeedSnap />
    </div>
  </div>
</template>

<script>

import Nav from './Nav.vue'
import FeedSnap from './FeedSnap.vue'

export default {

  components: {
    'Nav': Nav,
    'FeedSnap': FeedSnap
  },
  data () {
    return {
      topSnaps: ['funny cat', 'funny dog', 'funny dude']
    }
  }
}
</script>

<style scoped>
  h2 {
    color: red
  }
</style>
