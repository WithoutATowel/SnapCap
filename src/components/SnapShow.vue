<template>
  <div class="hello">
    <p>Img goes here!!!!!!</p>
    <div v-for='cap in captions'>
      <Caption />
    </div>
  </div>
</template>

<script>

import Caption from './Caption.vue'

export default {
  components: {
    'Caption': Caption
  },
  data () {
    return {
      captions: ['funny cat', 'funny dog', 'funny dude']
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
</style>
