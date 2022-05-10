<template>
  <div @click="sendData">
    <img :src="video.snippet.thumbnails.default.url" alt="">
    <span>{{ video.snippet.title }}</span>
  </div>
</template>

<script>
export default {
  name:'VideoListItem',
  props:{
    video:Object,
  },
  methods: {
    sendData(){
      this.$emit('send-data', this.video)
    }
  }
}
</script>

<style>

</style>