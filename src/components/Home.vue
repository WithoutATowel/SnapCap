<template>
  <div class="row">
    <ul class="tabs">
      <li class="tab col s2"><a class="active" v-on:click="getAll" href="#all">All</a></li>
      <li class="tab col s2"><a v-on:click="getAnimals" href="#animals">Animals</a></li>
      <li class="tab col s2"><a v-on:click="getCats" href="#cats">Cats</a></li>
      <li class="tab col s2"><a v-on:click="getDogs" href="#dogs">Dogs</a></li>
      <li class="tab col s2"><a v-on:click="getSports" href="#sports">Sports</a></li>
      <li class="tab col s2"><a v-on:click="getHummus" href="#hummus">Hummus</a></li>
    </ul>
    <div v-for='snap in snaps' :key='snap.id'>
      <FeedSnap v-bind:snap="snap" />
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import FeedSnap from './FeedSnap.vue'

export default {

  components: {
    'FeedSnap': FeedSnap
  },
  data () {
    return {
      snaps: [],
      topCap: null
    }
  },
  methods: {
    getAll: function () {
      console.log('clicked on All tab')
      axios.get('/api/api/snaps/')
        .then((response) => {
          this.snaps = response.data
          console.log('here is response.data (snaps): ', response.data)
        })
    },
    getAnimals: function () {
      console.log('clicked on Animals tab')
      axios.get('/api/api/snaps/animals/')
        .then((response) => {
          this.snaps = response.data
        })
    },
    getCats: function () {
      console.log('clicked on Cats tab')
      axios.get('/api/api/snaps/cats/')
        .then((response) => {
          this.snaps = response.data
        })
    },
    getDogs: function () {
      console.log('clicked on Dogs tab')
      axios.get('/api/api/snaps/dogs/')
        .then((response) => {
          this.snaps = response.data
        })
    },
    getSports: function () {
      console.log('clicked on Sports tab')
      axios.get('/api/api/snaps/sports/')
        .then((response) => {
          this.snaps = response.data
        })
    },
    getHummus: function () {
      console.log('clicked on Hummus tab')
      axios.get('/api/api/snaps/hummus/')
        .then((response) => {
          this.snaps = response.data
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
