<template>
  <div>
    <h5>USERNAME's Snaps</h5>
    <Snap />
  </div>
</template>

<script>

import Snap from './Snap.vue'

export default {
  // props: ['cap'],
  components: {
    Snap
  },
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
</script>

<style scoped>



</style>
