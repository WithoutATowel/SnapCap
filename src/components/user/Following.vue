<template>
  <div class='friend-container'>
    <router-link :to="{ name: 'Profile', params: { id: friend.id } }">
      <img :src='friend.profile.profile_img' />
    </router-link>
    <span>{{ friend.username }}</span>
  </div>
</template>

<script>

export default {
  props: ['friend']
}
</script>

<style scoped>

img {
  max-width: 15%;
}

span {
  display: inline-block;
  position: relative;
  bottom: 1.5em;
  margin-left: 3em;
}

.friend-container {
  padding: 1em;
  background: #FFD216;
}

</style>
