<template>
  <div class="snap-show">
    <img :src='url' />
    <p>By <router-link :to="{ name: 'Profile', params: { id: user } }">{{ submitter }}</router-link></p>
    <form v-on:submit.prevent="submitCap">
      <input type="text" v-model="newCaption" placeholder="Your caption here..." />
      <button type="submit">Submit Caption</button>
    </form>
    <div v-for='cap in usercaps'>
      <Caption :cap='cap' />
    </div>
  </div>
</template>

<script>
import Caption from './Caption.vue'
import axios from 'axios'

export default {
  props: ['id'],
  components: {
    Caption
  },
  data () {
    return {
      newCaption: '',
      url: '',
      user: '',
      submitter: '',
      usercaps: []
    }
  },
  methods: {
    submitCap () {
      axios.post('/api/api/caps/', {
        user: this.$store.state.user.id,
        picture: this.id,
        text: this.newCaption,
        votes: 0
      }, {
        headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
      }).then((response) => {
        this.newCaption = ''
        this.usercaps.push(response.data)
        // console.log('Cap created', response.data)
      }).catch((err) => {
        console.log(err.response)
      })
    }
  },
  mounted () {
    // console.log('mounted')
    axios.get('/api/api/snaps/' + this.id + '/')
      .then((response) => {
        this.url = response.data.cloudinary_url
        this.user = response.data.user
        this.submitter = response.data.submitter
        this.usercaps = response.data.usercaps
        // console.log('here is response.data (snaps): ', response.data)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

body {
  display: flex;
  align-items: center;
  justify-content: center;
}

img {
  width: 40%;
}

.snap-show {
  padding: 1em;
  background-color: rgba(38, 232, 156, .4);
}
.caption {
  margin: 2em;
  padding: .3em 1.5em;
  background: #FFD216;
  color: white;
}

</style>
