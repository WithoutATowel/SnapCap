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
    <v-dialog/>
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
      // this.$store.dispatch('refreshToken')
      this.$store.dispatch('inspectToken')
    } else {
      localStorage.removeItem('t')
      localStorage.removeItem('u')
      this.$store.dispatch('logout')
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
button:hover {
  cursor: pointer;
}
.main-modal {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

nav .v--modal-box.v--modal form {
  height: initial;
}

.yellow-btn, button.yellow-btn {
  background: #f9de70;
}
.yellow-btn:hover, button .yellow-btn:hover, .yellow-btn:focus, button .yellow-btn:focus {
  background: #FFD216;
}

button.header-button {
  background: rgba(255, 255, 255, 0.51);
  border: none;
  border-radius: 2px;
}
button.header-button:hover {
  background: rgb(255, 255, 255);
}

</style>
