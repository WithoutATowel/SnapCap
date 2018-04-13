<template>
  <div>
    <p v-if="$store.state.user"><button v-on:click="show" class="header-button">Post</button></p>

    <modal name="post">
      <div class="main-modal">
        <form v-on:submit.prevent="onSubmit">
          <div class="modal-content">
            <input type="file" id="file" name="file" placeholder="image" />
            <select id="category" v-model="category">
              <option value="" disabled>Category</option>
              <option value="animals">Animals</option>
              <option value="cats">Cats</option>
              <option value="dogs">Dogs</option>
              <option value="sports">Sports</option>
              <option value="hummus">Hummus</option>
            </select>
          </div>
          <div class="modal-footer">
            <button type="submit" class="yellow-btn btn-flat">Post</button>
          </div>
        </form>
      </div>
    </modal>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      category: '',
      user: 'NO USER',
      cloudinary: {
        uploadPreset: 'urj196d3',
        apiKey: process.env.Cloudinary_API_KEY,
        cloudName: 'https://api.cloudinary.com/v1_1/dpa63jimp/upload'
      },
      thumbs: []
    }
  },
  methods: {
    onSubmit () {
      this.$modal.hide('post')
      const formData = new FormData()
      let fileInput = document.getElementById('file')
      formData.append('file', fileInput.files[0])
      formData.append('upload_preset', this.cloudinary.uploadPreset)
      formData.append('tags', 'gs-vue,gs-vue-uploaded')
      axios.post(this.cloudinary.cloudName, formData).then(res => {
        this.thumbs.unshift({
          url: res.data.secure_url
        })
        this.postSnap(res.data.secure_url, this.category)
      })
    },
    postSnap (url, category) {
      axios.post('/api/api/snaps/', {
        user: this.$store.state.user.id,
        cloudinary_url: url,
        category: category
      }, {
        headers: {'Authorization': 'JWT ' + this.$store.state.jwt}
      }).then((response) => {
      })
    },
    show () {
      this.$modal.show('post')
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
</style>
