<template>
  <div>
    <p>Login/Signup</p>
    <p>{{ user }}</p>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: ['NO USER']
    }
  }
}
</script>

<style scoped>
  h2 {
    color: red
  }
</style>
