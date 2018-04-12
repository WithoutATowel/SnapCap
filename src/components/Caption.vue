<template>
  <div class='caption row valign-wrapper'>
    <Vote v-bind:votes='cap.votes' v-bind:snap_id="cap.picture" v-bind:cap_id="cap.id" v-bind:element_type="'cap'" />
    <div class='caption-box col s9 l10'>
      "{{ cap.text }}"
      <router-link :to="{ name: 'Profile', params: { id: cap.user } }">by {{ cap.submitter }}</router-link>
    </div>
  </div>
</template>

<script>

import Vote from './Vote.vue'

export default {
  props: ['cap'],
  components: {
    Vote
  }
}
</script>

<style scoped>

.caption-box {
  display: inline-block;
  margin-left: 5px;
}

</style>
