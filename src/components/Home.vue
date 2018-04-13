 <template>
  <div class="row">
    <div class="tabs-row-7" v-if="$store.state.user">
      <input id="all-tab" type="radio" name="tabs" v-on:click="getFeed('all')" checked>
      <label for="all-tab" class="col s7ths">All</label>
      
      <input id="feed-tab" type="radio" name="tabs" v-on:click="getFeed(`friends/${$store.state.user.id}`)">
      <label for="feed-tab" class="col s7ths">My Feed</label>

      <input id="animals-tab" type="radio" v-on:click="getFeed('animals')" name="tabs">
      <label for="animals-tab" class="col s7ths">Animals</label>

      <input id="cats-tab" type="radio" v-on:click="getFeed('cats')" name="tabs">
      <label for="cats-tab" class="col s7ths">Cats</label>

      <input id="dogs-tab" type="radio" v-on:click="getFeed('dogs')" name="tabs">
      <label for="dogs-tab" class="col s7ths">Dogs</label>

      <input id="sports-tab" type="radio" v-on:click="getFeed('sports')" name="tabs">
      <label for="sports-tab" class="col s7ths">Sports</label>

      <input id="hummus-tab" type="radio" v-on:click="getFeed('hummus')" name="tabs">
      <label for="hummus-tab" class="col s7ths">Hummus</label>
    </div>
    <div class="tabs-row-6" v-else>
      <input id="all-tab" type="radio" name="tabs" v-on:click="getFeed('all')" checked>
      <label for="all-tab" class="col s7ths">All</label>

      <input id="animals-tab" type="radio" v-on:click="getFeed('animals')" name="tabs">
      <label for="animals-tab" class="col s7ths">Animals</label>

      <input id="cats-tab" type="radio" v-on:click="getFeed('cats')" name="tabs">
      <label for="cats-tab" class="col s7ths">Cats</label>

      <input id="dogs-tab" type="radio" v-on:click="getFeed('dogs')" name="tabs">
      <label for="dogs-tab" class="col s7ths">Dogs</label>

      <input id="sports-tab" type="radio" v-on:click="getFeed('sports')" name="tabs">
      <label for="sports-tab" class="col s7ths">Sports</label>

      <input id="hummus-tab" type="radio" v-on:click="getFeed('hummus')" name="tabs">
      <label for="hummus-tab" class="col s7ths">Hummus</label>
    </div>
    <div class='feed-snap-cont' v-for='snap in snaps' :key='snap.id'>
      <FeedSnap class='feed-snap' v-bind:snap="snap" />
    </div>
  </div>
</template>

<script>

import axios from 'axios'
import FeedSnap from './FeedSnap.vue'

export default {

  components: {
    'FeedSnap': FeedSnap
  },
  data () {
    return {
      snaps: [],
      topCap: null
    }
  },
  methods: {
    getFeed: function (category) {
      if (category === 'all') {
        axios.get('/api/api/snaps/')
          .then((response) => {
            this.snaps = response.data
          })
      } else {
        axios.get('/api/api/snaps/' + category + '/')
          .then((response) => {
            this.snaps = response.data
          })
      }
    }
  },
  mounted () {
    axios.get('/api/api/snaps/')
      .then((response) => {
        this.snaps = response.data
      })
  }
}
</script>

<style scoped>

.feed-snap {
  padding: 1em;
  background-color: rgba(38, 232, 156, .4);
  display: flex;
  align-items: center;
}

.feed-snap-cont:nth-child(2) {
  border-top: 1px solid #adf6d4;
  margin-top: 0px;
}

input {
  display: none;
}

.tabs-row-6 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
  margin-bottom: 0px;
}

.tabs-row-7 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
  margin-bottom: 0px;
}

label {
  display: inline-block;
  margin: 0 0 -1px;
  padding: 15px 25px !important;
  font-weight: 600;
  text-align: center;
  color: #bbb;
  border: 1px solid #f0f0f0;
  background: #f7f7f7;
  border-top: 2px solid #ddd;
  border-bottom: 0px;
  font-size: 1.1rem;
}

label:before {
  font-family: 'Font Awesome 5 Pro';
  font-weight: normal;
  margin-right: 10px;
}

label[for='all-tab']:before { content: '\f036'; }
label[for='feed-tab']:before { content: '🍜'; }
label[for*='animals-tab']:before { content: '🐮'; }
label[for*='cats-tab']:before { content: '🐱'; }
label[for*='dogs-tab']:before { content: '🐶'; }
label[for*='sports-tab']:before { content: '🏅'; }
label[for*='hummus-tab']:before { content: '👽'; }

label:hover {
  color: #888;
  cursor: pointer;
}

input:checked + label {
  color: #555;
  border: 1px solid #adf6d4;
  border-top: 2px solid #700048;
  border-bottom: 1px solid #adf6d4;
  background: #adf6d4;
}

@media screen and (max-width: 996px) {
  label {
    font-size: 1rem;
  }
}

@media screen and (max-width: 875px) {
  label {
    font-size: .8rem;
  }
}

@media screen and (max-width: 800px) {
  label {
    font-size: .6rem;
  }
}

@media screen and (max-width: 700px) {
  label {
    font-size: 1rem;
  }
  label:before {
    display: block;
    margin: 0px;
  }
}

@media screen and (max-width: 650px) {
  label {
    font-size: 0;
  }
  label:before {
    margin: 0;
    font-size: 18px;
  }
}

@media screen and (max-width: 400px) {
  label {
    padding: 15px;
  }
}

</style>
