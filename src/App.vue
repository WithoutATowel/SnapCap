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
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
html {
  height: 100%;
}

body {
  height: 100%;
}

main {
  margin-top: 10px;
}

#app {
  color: #2c3e50;
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}
</style>
