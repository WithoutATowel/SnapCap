<template>
  <div class="nav">
    <nav>
      <div class="row">
        <div class="col s4">
          <Logged />
        </div>
        <div class="col s4">
          <h5><router-link to='/' id="snap-cap">SnapCap</router-link></h5>
        </div>
        <div class="links col s4" v-if="$store.state.user">
          <Post class="post-btn" /> |
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

<style scoped>
h1 {
  color: #42b983;
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
  margin: 0 10px;
  color: white !important;
}

a:hover {
  border-bottom: 2px solid #FFD216;
}

.post-btn {
  display: inline-block;
}

#snap-cap {
  font-family: 'Gamja Flower', cursive;
  font-size: 1.5em;
}

#snap-cap:hover {
  border-bottom: none;
  font-weight: bold;
}

</style>
