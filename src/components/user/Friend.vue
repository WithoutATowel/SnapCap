<template>
  <div>
    <p>friend id: {{ friend.friend }}</p>
  </div>
</template>

<script>

// import Vote from './Vote.vue'

export default {
  props: ['friend'],
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
