<template>
  <div>
    <h2 v-for='friend in friends'>{{ friend }}</h2>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        friends: ['Scott', 'Sean', 'Brett'],
        msg: 'Hey there',
      }
    }
  }
</script>

<style scoped>
  h2 {
    color: red
  }
</style>
