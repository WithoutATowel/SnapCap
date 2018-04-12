<template>
  <div>
    <p v-if="$store.state.user"><button @click="show" class="header-button">Update Snappie</button></p>

    <modal name="update-biopic">
      <div class="main-modal">
        <form v-on:submit.prevent="onSubmit">
          <div class="modal-content">
            <input type="file" id="biopic" name="biopic" placeholder="image" />
          </div>
          <div class="modal-footer">
            <button type="submit" class="yellow-btn btn-flat">Update Snappie</button>
          </div>
        </form>
      </div>
    </modal>

  </div>
</template>

<script>
import axios from 'axios'

// Cloudinary credentials:
// Email: snapcap.ga@gmail.com
// Gmail password: capthemsnaps
// Cloudinary password: capthemsnaps

export default {
  props: ['getUser'],
  data () {
    return {
      user: 'NO USER',
      cloudinary: {
        uploadPreset: 'urj196d3',
        apiKey: '697457472426285',
        cloudName: 'https://api.cloudinary.com/v1_1/dpa63jimp/upload'
      },
      thumbs: []
    }
  },
  methods: {
    onSubmit () {
      this.$modal.hide('update-biopic')
      const formData = new FormData()
      let biopicInput = document.getElementById('biopic')
      formData.append('file', biopicInput.files[0])
      formData.append('upload_preset', this.cloudinary.uploadPreset)
      formData.append('tags', 'gs-vue,gs-vue-uploaded')
      axios.post(this.cloudinary.cloudName, formData).then(res => {
        this.thumbs.unshift({
          url: res.data.secure_url
        })
        this.updateBioPic(res.data.secure_url)
      })
    },
    updateBioPic (url) {
      axios.put(`/api/api/profile/${this.$store.state.user.profile.id}/`, {
        user: this.$store.state.user.id,
        profile_img: url
      }, {
        headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
      }).then((response) => {
        this.getUser()
      })
    },
    show () {
      this.$modal.show('update-biopic')
    }
  }
}
</script>

<style scoped>



</style>
