<template>
  <div>
    <h5>{{ username }}'s Caps</h5>
    <div v-for='cap in usercaps'>
      <Cap class='cap' :cap='cap' />
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
  props: ['username', 'id'],
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
      axios.get(`/api/user/${this.$route.params.id}/caps/`)
        .then((response) => {
          this.usercaps = response.data
        })
    }
  },
  watch: {
    '$route' (to, from) {
      if (from !== to) {
        this.getCapsList()
      }
    }
  }
}
</script>

<style scoped>

.cap {
  margin: 1em 0;
}

</style>
