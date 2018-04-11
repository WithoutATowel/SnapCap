<template>
  <div>
    <h5>{{ user_first }}'s Friends</h5>
    <div v-for='friend in friends'>
      <Friend :friend='friend' />
    </div>
  </div>
</template>

<script>

import Friend from './Friend.vue'

export default {
  props: ['user_first', 'friends'],
  components: {
    Friend
  },
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
</script>

<style scoped>



</style>
