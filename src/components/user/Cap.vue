<template>
  <div>
    <router-link :to="{ name: 'SnapShow', params: { id: cap.picture } }">
      <img :src='cap.picture__cloudinary_url' />
    </router-link>
    <p>{{ cap.text }}</p>
    <p>number of votes: {{ cap.votes }}</p>
    <!-- <hr /> -->
  </div>
</template>

<script>

export default {
  props: ['cap']
}
</script>

<style scoped>

img {
  width: 20%;
}

</style>
