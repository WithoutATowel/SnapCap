<template>
  <div>
    <h5>USERNAME's Caps</h5>
    <Cap />
  </div>
</template>

<script>

import Cap from './Cap.vue'

export default {
  // props: ['cap'],
  components: {
    Cap
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
