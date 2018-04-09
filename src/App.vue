<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <div class="container">
        <router-view/>
      </div>
    </main>
    <footer>
      <Footer />
    </footer>
    <button v-on:click="getSnaps">Get Snaps</button>
    <img v-for='snap in snaps' :key='snap.id' v-bind:src='snap.cloudinary_url' />
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'app',
  data () {
    return {
      snaps: []
    }
  },
  methods: {
    getSnaps: function () {
      console.log('clicked on getSnaps')
      axios.get('/api/api/snaps/')
        .then((response) => {
          this.snaps = response.data
          console.log(response.data)
          console.log(response.data[0].cloudinary_url)
        })
    }
  }
}
</script>

<style>
html {
  height: 100%;
}

body {
  /* display: flex; */
  /* align-items: center; */
  /* justify-content: center; */
  height: 100%;
}

main {
  margin-top: 10px;
}
img {
  max-width: 100%;
}
#app {
  color: #2c3e50;
  /* margin-top: -100px; */
  /* max-width: 600px; */
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  /* text-align: center; */
}

#app a {
  color: #42b983;
  /* text-decoration: none; */
}
</style>
