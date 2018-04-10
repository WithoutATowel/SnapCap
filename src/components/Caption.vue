<template>
  <div>
    <Vote v-bind:votes="'150'" v-bind:element_id="cap.id" v-bind:element_type="'cap'"  />
    <p class='caption-p'>{{ cap.text }}</p>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  props: ['cap'],
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

.caption-p {
  display: inline-block;
  margin-left: 3em;
}

</style>
