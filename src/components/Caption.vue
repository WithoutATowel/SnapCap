<template>
  <div>
    <Vote v-bind:votes='cap.votes' v-bind:element_id="cap.id" v-bind:element_type="'cap'"  />
    <div class='caption-box'>
      <p>"{{ cap.text }}"</p>
      <p>number of votes: {{ cap.votes }}</p>
    </div>
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

.caption-box {
  display: inline-block;
  margin-left: 3em;
}

</style>
