<template>
  <div>
    <ul class="tabs">
      <li class="tab col s3"><a href="#all">All</a></li>
      <li class="tab col s3"><a class="active" href="#animals">Animals</a></li>
      <li class="tab col s3"><a href="#cats">Cats</a></li>
      <li class="tab col s3"><a href="#dogs">Dogs</a></li>
      <li class="tab col s3"><a href="#sports">Sports</a></li>
      <li class="tab col s3"><a href="#hummus">Hummus</a></li>
    </ul>
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
