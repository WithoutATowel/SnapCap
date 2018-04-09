<template>
  <div class="hello">
    <Logged />
    <a href='/#/'>Home</a>
    <br />
    <a href='/#/snaps'>Snap Show</a>
    <Search />
  </div>
</template>

<script>

import Logged from './Logged.vue'
import Search from './Search.vue'

export default {
  components: {
    'Logged': Logged,
    'Search': Search,
  },
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      msg: 'Hello World!!!1!'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
</style>
