<template>
  <div class="row">
    <div class="col s3 m2 l1">
        <Vote v-if="snap.votes" v-bind:votes="snap.votes" v-bind:snap_id="snap.id" v-bind:cap_id="null"v-bind:element_type="'snap'" />
        <Vote v-if="!snap.votes" v-bind:votes="0" v-bind:snap_id="snap.id" v-bind:cap_id="null" v-bind:element_type="'snap'" />
    </div>
    <div class="each-snap col s9 m10 m11">
      <div class="row">
        <div class="col s12 m12 l5">
          <router-link :to="{ name: 'SnapShow', params: {
              id: snap.id,
            } }"><img v-bind:src='snap.cloudinary_url' />
          </router-link>
          <router-link :to="{ name: 'Profile', params: { id: snap.user } }"><p>Snapped by: {{snap.submitter}}</p></router-link>
        </div>

        <div class="col s12 m12 l7">
          <div class="top-cap-header row">
            <div class="col s5">
              <h5>Top Caption:</h5>
            </div>
            <div class="col s7">
              <p v-if='this.topCap' class="top-cap-details">
                Votes: {{ this.topCap.votes }} |
                <router-link v-if='this.topCap' :to="{ name: 'Profile', params: { id: this.topCap.user } }">Capped by: {{this.topCap.submitter}}</router-link>
              </p>
            </div>
          </div>
          <div class='top-cap-box'>
            <h3 v-if='this.topCap'>"{{ this.topCap.text }}"</h3>
            <h3 v-else>No Captions Yet...</h3>
          </div>
          <div class="row add-cap">
            <form v-on:submit.prevent="submitCap" >
              <div>
                <input type="text" v-model="newCaption" placeholder="Your caption here..." />
                <button type="submit" class="submit-caption">Submit Caption</button>
              </div>
            </form>
          </div>
          <div v-for="cap in snap.usercaps.slice(0,3)">
            <Caption v-bind:cap="cap" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Vote from './Vote.vue'
import Caption from './Caption.vue'
import axios from 'axios'
export default {
  mounted () {
    this.getTopSnap()
  },
  props: ['snap'],
  components: {
    Vote,
    Caption
  },
  data () {
    return {
      topCap: null,
      newCaption: ''
    }
  },
  methods: {
    getTopSnap: function () {
      let voteCount = 0
      this.snap.usercaps.forEach(cap => {
        if (cap.votes >= voteCount) {
          this.topCap = cap
          voteCount = cap.votes
        }
      })
    },
    submitCap () {
      axios.post('/api/api/caps/', {
        user: this.$store.state.user.id,
        picture: this.snap.id,
        text: this.newCaption,
        votes: 0
      }, {
        headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
      }).then((response) => {
        this.snap.usercaps.push(response.data)
        this.newCaption = ''
        if (!this.topCap) {
          this.topCap = response.data
        }
        console.log('Cap created', response.data)
      }).catch((err) => {
        console.log(err.response)
      })
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 10px 0px;
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
h5 {
  margin: 0px;
}
a {
  max-width: 40%;
}
img {
  max-width: 100%;
}
.top-cap-details {
  margin-top: 0px;
}
.each-snap {
  /* padding: 0 10%; */
  /* display: flex;
  align-content: center;
  justify-content: space-between; */
}

.top-cap-box {
  /* margin: 2em; */
  padding: .3em 1.5em;
  background: #f7f7f7;
  color: #333;
}

.caption {
  margin: 2em 0px;
  padding: .3em 0;
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

input[type="text"] {
  background: rgba(255,255,255,.5);
  margin: 0px;
  max-width: 70%;
}

::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: #000;
    opacity: .7; /* Firefox */
}

.add-cap {
  margin-top: 10px;
}
.add-cap div {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}

</style>
