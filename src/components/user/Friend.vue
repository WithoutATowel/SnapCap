<template>
  <div>
    <router-link :to="{ name: 'Profile', params: { id: friend.pk } }"><p>go to user profile for snap ~~CHANGE THIS TO THEIR IMG~~</p></router-link>
    </router-link>
    <p>{{ friend.fields.first_name }} {{ friend.fields.last_name }}</p>
  </div>
</template>

<script>

export default {
  props: ['friend']
}
</script>

<style scoped>



</style>
