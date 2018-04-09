<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <router-view/>
    </main>
    <footer>
      <Footer />
    </footer>
    <button v-on:click="getJokes">Get Snaps</button>
    <p v-for='joke in jokes' :key='joke.id'>{{ joke.joke }}</p>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'app',
  data () {
    return {
      jokes: []
    }
  },
  methods: {
    getJokes: function () {
      // axios.get('http://api.icndb.com/jokes/random/10')
      axios.get('/api/snaps')
        .then((response) => {
          this.jokes = response.data.value
          console.log(response.data)
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
