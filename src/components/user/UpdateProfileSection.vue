<template>
  <div>
    <p>Update Profile Section Component</p>
    <ChangeProfilePic />
    <EditProfile />
  </div>
</template>

<script>

import ChangeProfilePic from './ChangeProfilePic.vue'
import EditProfile from './EditProfile.vue'

export default {
  // props: ['cap'],
  components: {
    ChangeProfilePic,
    EditProfile
  }
}
</script>

<style scoped>



</style>
