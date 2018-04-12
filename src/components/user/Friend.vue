<template>
  <div class='friend-container'>
    <router-link :to="{ name: 'Profile', params: { id: friend.pk } }">
      <p>go to user profile for snap ~~CHANGE THIS TO THEIR IMG~~</p>
    </router-link>
    <p>{{ friend.fields.first_name }} {{ friend.fields.last_name }}</p>
  </div>
</template>

<script>

export default {
  props: ['friend', 'getUser']
}
</script>

<style scoped>

.friend-container {
  padding: 1em;
  background: #FFD216;
}

</style>
