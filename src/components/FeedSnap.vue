<template>
  <div>
    <Vote />
    <img v-bind:src='snap.cloudinary_url' />
    <p>Img goes here</p>
    <p>Cap goes here</p>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  props: ['snap'],
  components: {
    'Vote': Vote
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
