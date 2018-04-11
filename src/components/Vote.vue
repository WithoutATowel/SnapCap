<template>
  <div>
    <button v-on:click="upVote( element_type )">
      <div class="up-icon">
        <i class="fas fa-caret-circle-up"></i>
      </div>

      <div class="vote-num">{{ votes }}</div>
    </button>
  </div>

</template>

<script>
import axios from 'axios'
export default {
  props: ['votes', 'element_id', 'element_type'],
  data () {
    return {
      data: 'NO DATA'
    }
  },
  methods: {
    upVote (type) {
      // /api/vote_picture/
      if (type === 'snap') {
        axios.post('/api/api/vote_picture/', {user: this.$store.state.user.id, picture: this.element_id}, {headers: {'Authorization': 'JWT ' + this.$store.state.jwt}})
        .then(result => {
          // console.log('vote picture return data: ', result)
        }).catch(err => {
          if (err.response.data.non_field_errors[0] === 'The fields user, picture must make a unique set.') {
            this.$modal.show('dialog', {
              title: 'Alert!',
              text: 'You are only allowed to vote once per post.',
              buttons: [
                {
                  title: 'OK',
                  default: true
                }
              ]
            })
          }
          if (err.response.data.non_field_errors[0] === 'Signature has expired.') {
            this.$modal.show('dialog', {
              title: 'Alert!',
              text: 'You need to be logged in to do that',
              buttons: [
                {
                  title: 'OK',
                  default: true
                }
              ]
            })
          }
          console.log(err.response)
        })
      }
      if (type === 'cap') {
        console.log('You clicked to add a vote for a caption.... jokes on you, I haven\'t gotten ther yet')
        // axios.post('/api/api/vote_caption/', {user: this.$store.state.user.id, picture: this.element_id},  {headers: {'Authorization': 'JWT ' + this.$store.state.jwt}})
        // .then(result => {
        //   console.log('vote picture return data: ', result.data)
        // }).catch(err => {
        //   console.log(err)
        // })
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
  button {
    display: flex;
    align-items: center;
    background: none;
    border: none;
    color: #42b983;
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
