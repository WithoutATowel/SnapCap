<template>
  <div>
    <h5>{{ user_first }}'s Caps</h5>
    <div v-for='cap in usercaps'>
      <Cap :cap='cap' />
    </div>
  </div>
</template>

<script>

import Cap from './Cap.vue'

export default {
  props: ['user_first', 'usercaps'],
  components: {
    Cap
  },
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
</script>

<style scoped>



</style>
