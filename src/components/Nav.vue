<template>
  <div class="nav">
    <nav>
      <div class="row">
        <div class="col s4">
          <Logged />
        </div>
        <div class="col s4">
          <h5><router-link to='/'>SnapCap</router-link></h5>
        </div>
        <div class="links col s4">
          <div class="col">
            <Post />
          </div>
          <router-link v-if="$store.state.user" :to="{ name: 'Profile', params: { id: $store.state.user.id } }">Profile</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>

import Logged from './Logged.vue'
import Search from './Search.vue'
import Post from './Post.vue'

export default {
  components: {
    'Logged': Logged,
    'Search': Search,
    'Post': Post
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
.col {
  text-align: center;
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
