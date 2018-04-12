<!-- <template>
  <div>
      <button v-on:click="show('edit')" class="header-button">Signup</button></p>

    <modal name="edit" height="auto" :scrollable="true" :adaptive="true">
      <div class="row-fluid">
        <div class="col s6">
          <div class="main-modal">
            <form v-on:submit.prevent="onEditSubmit('edit')">
              <div class="modal-content">
                <input type="text" name="first-name" v-model="edit['first_name']" placeholder="First Name"/>
                <input type="text" name="last-name" v-model="edit['last_name']" placeholder="Last Name"/>
                <input type="text" name="username" v-model="edit['username']" placeholder="Username" />
                <input type="text" name="email" v-model="edit['email']" placeholder="Email" />
                <input type="password" name="password" v-model="edit['password']" placeholder="Password" />
              </div>
              <div class="modal-footer">
                <button type="submit" class="yellow-btn btn-flat">Update Profile</button>
              </div>
            </form>
          </div>
        </div>
        <div class="col s6 edit-img-cont">
          <img src="../../assets/edit.jpeg" />
        </div>
      </div>
    </modal>

  </div>

</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      user: 'NO USER',
      edit: {
        'username': this.$store.state.username,
        'first_name': this.$store.state.first_name,
        'last_name': this.$store.state.last_name,
        'email': this.$store.state.email
      }
    }
  },
  methods: {
    onEditSubmit () {
      axios.post('/api/api/users/', this.edit).then(result => {
        this.$modal.hide('edit')
        this.$store.dispatch('obtainToken', [result.data.username, this.edit.password])
      }).catch(err => {
        console.log(err.response)
      })
    },
    show (type) {
      this.$modal.show(type)
    }
  }
}
</script>

<style scoped>

  h2 {
    color: red
  }

  p {
    margin: 0px;
  }

  .username {
    display: inline-block;
    font-size: 1.2rem;
  }

  .edit-img-cont {
    display: flex;
    justify-content: center;
    align-items: center;
    max-height: 100%;
    overflow: hidden;
  }

  .edit-img-cont img {
    width: auto;
    height: 100%;
    max-width: initial;
  }

  .row-fluid, .s6 {
    height: 100%;
  }

  .main-modal {
    height: 100%
  }

</style> -->
