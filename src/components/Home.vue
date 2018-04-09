<template>
  <div class="row">
    <ul class="tabs">
      <li class="tab col s2"><a class="active" v-on:click="getAll" href="#all">All</a></li>
      <li class="tab col s2"><a href="#animals">Animals</a></li>
      <li class="tab col s2"><a href="#cats">Cats</a></li>
      <li class="tab col s2"><a href="#dogs">Dogs</a></li>
      <li class="tab col s2"><a href="#sports">Sports</a></li>
      <li class="tab col s2"><a href="#hummus">Hummus</a></li>
    </ul>
    <div v-for='snap in snaps' :key='snap.id'>
      <FeedSnap v-bind:snap="snap" />
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import Nav from './Nav.vue'
import FeedSnap from './FeedSnap.vue'

export default {

  components: {
    'Nav': Nav,
    'FeedSnap': FeedSnap
  },
  data () {
    return {
      snaps: []
    }
  },
  methods: {
    getAll: function () {
      // axios.get('http://api.icndb.com/jokes/random/10')
      console.log('clicked on getSnaps')
      axios.get('/api/api/snaps/')
        .then((response) => {
          this.snaps = response.data
          console.log(response.data)
          console.log(response.data[0].cloudinary_url)
        })
    }
  }
}
</script>

<style scoped>
  h2 {
    color: red
  }
</style>
