<template>
  <div>
    <!-- <router-link :to="{ name: 'SnapShow', params: {
        id: snap.id,
        url: snap.cloudinary_url,
        user: snap.user,
        usercaps: snap.usercaps
      } }"><img :src='snap.cloudinary_url' />
    </router-link> -->
    <!-- <router-link :to="{ name: 'Profile', params: { id: snap.user } }"><p>go to user profile for snap</p></router-link> -->
    <p>{{ cap.text }}</p>
    <p>number of votes: {{ cap.votes }}</p>
    <!-- <hr /> -->
  </div>
</template>

<script>

// import Vote from './Vote.vue'

export default {
  props: ['cap'],
  // components: {
  //   Friend
  // },
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
</script>

<style scoped>



</style>
