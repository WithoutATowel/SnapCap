<template>
  <div id="app">
    <header>
      <Nav />
    </header>
    <main>
      <div class="router-container container-fluid">
        <router-view />
      </div>
    </main>
    <footer>
      <Footer />
    </footer>
  </div>
</template>

<script>



export default {
  name: 'app',
  mounted () {
    if (localStorage.getItem('t')) {
      let token = localStorage.getItem('t')
      let user = localStorage.getItem('u')
      user = JSON.parse(user)
      this.$store.state.jwt = token
      this.$store.state.user = user
    } else {
      localStorage.removeItem('t')
      localStorage.removeItem('u')
      this.$store.dispatch('logout')
    }
  }
  // data () {
  //   return {
  //     snaps: []
  //   }
  // }
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
  flex: 1 0 auto;
  margin-top: 10px;
}

img {
  max-width: 100%;
}

select {
  display: block;
}

.router-container {
  padding: 1em 2em;

}

#app {
  color: #2c3e50;
  /* margin-top: -100px; */
  /* max-width: 600px; */
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  /* text-align: center; */
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

#app a {
  color: #42b983;
  /* text-decoration: none; */
}

</style>
