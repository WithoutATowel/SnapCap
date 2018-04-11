<template>
  <div>
    <h5>{{ user_first }}'s Snaps</h5>
    <div v-for='snap in snaps'>
      <Snap :snap='snap' />
    </div>
  </div>
</template>

<script>

import Snap from './Snap.vue'

export default {
  props: ['user_first', 'snaps'],
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
