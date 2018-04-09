<template>
  <div>
    <p><a class="modal-trigger" href="#login">Login</a>/<a class="modal-trigger" href="#signup">Signup</a> | {{ user }}</p>

    <!-- Modal Structure -->
    <div id="login" class="modal">
      <form>
        <div class="modal-content">
          <input type="text" placeholder="Email" />
          <input type="password" placeholder="Password" />
        </div>
        <div class="modal-footer">
          <button type="submit" class="modal-action modal-close waves-effect waves-green btn-flat">Login</button>
        </div>
      </form>
    </div>

    <div id="signup" class="modal">
      <form>
        <div class="modal-content">
          <input type="text" name="name" placeholder="Name"/>
          <input type="text" name="username" placeholder="Username" />
          <input type="text" name="email" placeholder="Email" />
          <input type="password" name="password" placeholder="Password" />
        </div>
        <div class="modal-footer">
          <button type="submit" class="modal-action modal-close waves-effect waves-green btn-flat">Sign Up</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: 'NO USER'
    }
  }
}
</script>

<style scoped>
  h2 {
    color: red
  }
  p {
    margin: 0px;
  }
</style>
