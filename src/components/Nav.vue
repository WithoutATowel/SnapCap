<template>
  <div class="nav">
    <nav>
      <div class="row">
        <div class="col s4">
          <Logged />
        </div>
        <div class="col s4">
          <h5>SnapCap</h5>
        </div>
        <div class="links col s4">
          <router-link to='/'>Home</router-link>
          <router-link to='/profile'>Profile</router-link>
          <Search />
        </div>
      </div>
    </nav>


  </div>
</template>

<script>

import Logged from './Logged.vue'
import Search from './Search.vue'

export default {
  components: {
    'Logged': Logged,
    'Search': Search
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

a {
  margin: 0 10px;
}

nav {
  background-color: #26E89C;
  box-shadow: none;
}

a {
  padding: .2em .1em;
  color: white !important;
}

a:hover {
  border-bottom: 2px solid #FFD216;
}

.search-cont {
  display: inline-block;
}

</style>
