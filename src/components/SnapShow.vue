<template>
  <div class="snap-show row">
    <div class="col s12 m12 l6">
      <img :src='url' />
      <p class='snapped-by'><router-link :to="{ name: 'Profile', params: { id: user } }"><span>Snapped By: {{ submitter }}</span></router-link></p>
    </div>
    <div class="col s12 m12 l6">
      <div class="row add-cap">
        <div class="top-cap-header">
          <h5>Cap This Snap</h5>
        </div>
        <form v-on:submit.prevent="submitCap" >
          <div>
            <input type="text" v-model="newCaption" placeholder="Your caption here..." />
            <button type="submit" class="submit-caption">Submit Caption</button>
          </div>
        </form>
      </div>
      <div v-for='cap in usercaps'>
        <Caption :cap='cap' />
      </div>
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
      }).catch((err) => {
        console.log(err.response)
      })
    }
  },
  mounted () {
    axios.get('/api/api/snaps/' + this.id + '/')
      .then((response) => {
        this.url = response.data.cloudinary_url
        this.user = response.data.user
        this.submitter = response.data.submitter
        this.usercaps = response.data.usercaps
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
h5 {
  margin: 0;
}
.snapped-by {
  margin: 5px 0px 0px;
}
.snapped-by span {
  background: #fff;
  padding: 5px;
  border-radius: 4px;
  text-transform: capitalize;
  font-weight: 600;
}
.snap-show {
  padding: 1em;
  background-color: rgba(38, 232, 156, .4);
}
.caption {
  margin: 2em 0px;
  padding: .3em 1.5em;
  background: #FFD216;
  color: white;
}
.submit-caption {
  background: #222;
  border: none;
  color: #fff;
  padding: 14px 15px 15px;
}
.submit-caption:hover,.submit-caption:focus {
    background: #222;
    border: none;
    color: #44e993;
}
.top-cap-header {
  background: #730046;
  color: #fff;
  padding: 6px;
  margin: 0px;
  display: flex;
  align-items: center;
}
.top-cap-header p {
  margin: 0px;
  text-align: right;
}
input[type="text"] {
  background: rgba(255,255,255,1);
  margin: 0px;
  max-width: 70%;
}
.add-cap {
  margin-top: 10px;
  background: #f7f7f7;
  margin: 14px 0px 0px 0px;
  padding: 0px 0px 12px;
}
.add-cap div {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.add-cap .top-cap-header {
  margin-top: -12px;
  margin-bottom: 10px;
  justify-content: baseline;
  padding-left: 20px;
}
@media screen and (min-width: 993px) {
  .snap-show {
    display: flex;
  }
  .snap-show > div {
    flex: 1;
  }
}
</style>
