<template>
  <div>
    <Vote />
    <p class='caption-p'>{{ cap }}</p>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  props: ['cap'],
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

.caption-p {
  display: inline-block;
  margin-left: 3em;
}

</style>
