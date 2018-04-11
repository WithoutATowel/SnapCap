<template>
  <div class="row">
    <div class="col s1">
        <Vote v-if="snap.votes" v-bind:votes="snap.votes" v-bind:snap_id="snap.id" v-bind:cap_id="null"v-bind:element_type="'snap'" />
        <Vote v-if="!snap.votes" v-bind:votes="0" v-bind:snap_id="snap.id" v-bind:cap_id="null" v-bind:element_type="'snap'" />
    </div>
    <div class="each-snap col s12">
      <router-link :to="{ name: 'SnapShow', params: {
          id: snap.id,
        } }"><img v-bind:src='snap.cloudinary_url' />
      </router-link>
      <router-link :to="{ name: 'Profile', params: { id: snap.user } }"><p>go to user profile for snap</p></router-link>
      <div class='top-cap-box'>
        <h5>Top Caption!</h5>
        <p v-if='this.topCap'>"{{ this.topCap.text }}"</p>
        <p v-if='this.topCap'>number of votes: {{ this.topCap.votes }}</p>
        <router-link v-if='this.topCap' :to="{ name: 'Profile', params: { id: this.topCap.user } }"><p>go to user profile for cap</p></router-link>
      </div>
    </div>
    <div class="col s1">
    </div>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  mounted () {
    this.getTopSnap()
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
    getTopSnap: function () {
      let voteCount = 0
      this.snap.usercaps.forEach(cap => {
        if (cap.votes > voteCount) {
          this.topCap = cap
          voteCount = cap.votes
        }
      })
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
