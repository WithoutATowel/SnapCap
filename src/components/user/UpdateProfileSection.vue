<template>
  <div>
    <ChangeProfilePic v-bind='{getUser}' />
    <!-- <EditProfile /> -->
  </div>
</template>

<script>

import ChangeProfilePic from './ChangeProfilePic.vue'
// import EditProfile from './EditProfile.vue'

export default {
  props: ['getUser'],
  components: {
    ChangeProfilePic
    // EditProfile
  }
}
</script>

<style scoped>



</style>
