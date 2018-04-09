<template>
  <div>
    <a href="#">
      <div class="up-icon">
        <i class="fas fa-caret-circle-up"></i>
      </div>
      <div class="vote-num">150</div>
    </a>
  </div>


</template>

<script>
export default {
  data () {
    return {
      data: 'NO DATA'
    }
  }
}
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
