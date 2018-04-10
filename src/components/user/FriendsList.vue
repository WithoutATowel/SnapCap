<template>
  <div>
    <h5>USERNAME's Friends</h5>
    <Friend />
  </div>
</template>

<script>

import Friend from './Friend.vue'

export default {
  // props: ['cap'],
  components: {
    Friend
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
