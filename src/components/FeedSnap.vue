<template>
  <div class="row">
    <div class="col s1">
      <Vote v-bind:votes="snap.usercaps[0].votes" v-bind:element_id="snap.id" v-bind:element_type="'snap'" />
    </div>
    <div class="each-snap col s12">
      <router-link :to="{ name: 'SnapShow', params: {
          id: snap.id,
          url: snap.cloudinary_url,
          usercaps: snap.usercaps
        } }"><img v-bind:src='snap.cloudinary_url' />
      </router-link>
      <div class='top-cap-box'>
        <h5>Top Caption!</h5>
        <p v-if='this.topCap'>"{{ this.topCap.text }}"</p>
        <p v-if='this.topCap'>number of votes: {{ this.topCap.votes }}</p>
      </div>
    </div>
    <div class="col s1">
    </div>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  mounted() {
    this.findTopSnap()
  },
  props: ['snap'],
  components: {
    Vote
  },
  data () {
    return {
      topCap: null
    }
  },
  methods: {
    findTopSnap: function () {
      let voteCount = 0
      this.snap.usercaps.forEach(cap => {
        if (cap.votes > voteCount) {
          this.topCap = cap
          voteCount = cap.votes
        }
      })
      console.log(this.topCap)
    }
  }
}
</script>

<style scoped>

h5 {
  color: #730046;
}

a {
  max-width: 40%;
}

img {
  max-width: 100%;
}

.each-snap {
  padding: 0 10%;
  display: flex;
  align-content: center;
  justify-content: space-between;
}

.top-cap-box {
  margin: 2em;
  padding: .3em 1.5em;
  background: #FFD216;
  color: white;
}

</style>
