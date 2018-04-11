<template>
  <div>
    <a href="#" v-on:click="upVote( element_type )">
      <div class="up-icon">
        <i class="fas fa-caret-circle-up"></i>
      </div>

      <div class="vote-num">{{ votes }}</div>
    </a>
  </div>

</template>

<script>
import axios from 'axios'
export default {
  props: ['votes', 'snap_id', 'cap_id', 'element_type'],
  data () {
    return {
      data: 'NO DATA'
    }
  },
  methods: {
    upVote (type) {
      // /api/vote_picture/
      if (type === 'snap') {
        axios.post('/api/api/vote_picture/', {user: this.$store.state.user.id, picture: this.snap_id}, {headers: {'Authorization': 'JWT ' + this.$store.state.jwt}})
        .then(result => {
          console.log('vote picture return data: ', result.data)
        }).catch(err => {
          console.log(err)
        })
      }
      if (type === 'cap') {
        axios.post('/api/api/vote_caption/', {user: this.$store.state.user.id, picture: this.snap_id, usercap: this.cap_id},  {headers: {'Authorization': 'JWT ' + this.$store.state.jwt}})
        .then(result => {
          console.log('vote picture return data: ', result.data)
        }).catch(err => {
          console.log(err)
        })
      }
    }
  }
}
// For checking authorization:
// let options = this.$store.state.jwt ? {headers: {'Authorization': 'JWT ' + this.$store.state.jwt}} : ''
</script>

<style scoped>
  h2 {
    color: red
  }
  a {
    display: flex;
    align-items: center;
  }
  .up-icon {
    font-size: 2rem;
    z-index: 2;
  }
  i {
    background: white;
    border-radius: 100%;
  }
  .vote-num {
    background: #333;
    border-radius: 2px;
    padding: 0px 10px 0px 20px;
    margin-left: -10px;
  }
</style>
