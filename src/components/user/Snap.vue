<template>
  <div class='snap-container'>
    <router-link :to="{ name: 'SnapShow', params: {
        id: snap.id,
        url: snap.cloudinary_url,
        user: snap.user,
        usercaps: snap.usercaps
      } }"><img :src='snap.cloudinary_url' />
    </router-link>
    <p>pic votes: {{ snap.votes }}</p>
    <p v-if='this.topCap'>"{{ this.topCap.text }}"</p>
    <p v-if='this.topCap'>number of votes: {{ this.topCap.votes }}</p>
    <router-link v-if='this.topCap' :to="{ name: 'Profile', params: { id: this.topCap.user } }"><p>by {{ this.topCap.submitter }}</p></router-link>
  </div>
</template>

<script>

export default {
  mounted () {
    this.getTopSnap()
  },
  props: ['snap'],
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
      console.log('this.topCap: ', this.topCap)
    }
  },
  watch: {
    snap: function(newVal, oldVal) {
      this.getTopSnap();
    }
  }
}
</script>

<style scoped>

img {
  width: 50%;
}

.snap-container {
  padding: 1em;
  background: #FFD216;
}

</style>
