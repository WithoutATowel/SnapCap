<template>
  <div class="search-cont">
    <input type='text' placeholder='search' />
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
</script>

<style scoped>

input {
  color: #730046;
  font-weight: bold;
}

::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: #fff;
    opacity: .7; /* Firefox */
}

/* input:placeholder-shown {
  color: blue;
} */

</style>
