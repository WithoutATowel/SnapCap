<template>
  <div>
    <h5>{{ user_first }}'s Snaps</h5>
    <div v-for='snap in snaps'>
      <Snap class='snap' :snap='snap' />
    </div>
  </div>
</template>

<script>

import Snap from './Snap.vue'

export default {
  props: ['user_first', 'snaps'],
  components: {
    Snap
  }
}
</script>

<style scoped>

.snap {
  margin: 1em 0;
}

</style>
