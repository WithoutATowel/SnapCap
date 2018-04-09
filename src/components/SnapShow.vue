<template>
  <div class="snap-show">
    <p>Img goes here!!!!!!</p>
    <!-- <div v-for='cap in captions' :key='caption.id'> -->
    <div v-for='cap in captions'>
      <Caption class='caption' v-bind:cap='cap' />
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

body {
  display: flex;
  align-items: center;
  justify-content: center;
}

.snap-show {
  padding: 1em;
  background-color: rgba(38, 232, 156, .4);
}

.caption {
  margin: 2em;
  padding: .3em 1.5em;
  background: #FFD216;
  color: white;
}

</style>
