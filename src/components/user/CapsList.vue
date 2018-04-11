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
import axios from 'axios'

export default {
  mounted () {
    this.getCapsList()
  },
  props: ['user_first', 'id'],
  components: {
    Cap
  },
  data () {
    return {
      usercaps: []
    }
  },
  methods: {
    getCapsList: function () {
      axios.get(`/api/api/user/${this.id}/caps/`)
        .then((response) => {
          this.usercaps = response.data
          console.log('here is capslist comp response.data: ', response.data)
        })
    }
  }
}
</script>

<style scoped>



</style>
