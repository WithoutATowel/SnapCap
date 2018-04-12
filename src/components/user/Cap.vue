<template>
  <div class='cap-container'>
    <div class='row'>
      <div class='col s3'>
        <router-link :to="{ name: 'SnapShow', params: { id: cap.picture } }">
          <img :src='cap.picture__cloudinary_url' />
        </router-link>
      </div>
      <div class='col s9'>
        <div class='row'>
          <p>{{ cap.text }}</p>
        </div>
        <div class='row'>
          <p>number of votes: {{ cap.votes }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import Vote from '../Vote.vue'

export default {
  props: ['cap'],
  components: {
    Vote
  }
}
</script>

<style scoped>

img {
  width: 100%;
  display: inline-block;
  margin-right: .5em;
}

.cap-container {
  padding: 1em;
  background: #FFD216;
}

.vote {
  display: block;
}

.row {
  margin: 0;
}

</style>
