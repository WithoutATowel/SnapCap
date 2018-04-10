<template>
  <div>
    <p><a class="modal-trigger" href="#post">Post</a></p>

    <!-- Modal Structure -->
    <div id="post" class="modal">
      <form v-on:submit.prevent="onSubmit">
        <div class="modal-content">
          <input type="file" id="file" placeholder="image" />
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
          <button type="submit" class="modal-action modal-close waves-effect waves-green btn-flat">Post</button>
        </div>
      </form>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

// Cloudinary credentials:
// Email: snapcap.ga@gmail.com
// Gmail password: capthemsnaps
// Cloudinary password: capthemsnaps

export default {
  data () {
    return {
      category: '',
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
    onSubmit (e) {
      e.preventDefault()
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
      // console.log('user: ', $store.state.user.id)
      console.log('url: ', url)
      console.log('category: ', category)
      axios.post('/api/api/snaps/', {
        user: 5,
        cloudinary_url: url,
        category: category
      }).then((response) => {
        console.log('Snap created')
      })
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
