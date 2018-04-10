<template>
  <div class="row">
    <div class="col s1">
      <Vote />
    </div>
    <div class="col s10">
      <router-link :to="'/snaps/' + snap.id"><img v-bind:src='snap.cloudinary_url' /></router-link>
      <p>Cap goes here</p>
    </div>
    <div class="col s1">
    </div>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  props: ['snap'],
  components: {
    Vote
  },
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
</script>

<style scoped>
  h2 {
    color: red
  }
</style>
