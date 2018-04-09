<template>
  <div>
    <p>Login/Signup | {{ user }}</p>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        user: ['NO USER'],
      }
    }
  }
</script>

<style scoped>
  h2 {
    color: red
  }
  p {
    margin: 0px;
  }
</style>
