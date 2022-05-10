<template>
  <div>
    <iframe id="player" type="text/html" width="640" height="360"
    v-if="clickVideo"
      :src="playVideoUrl"
      frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name:'VideoDetail',
  props: {
    clickVideo:Object,
  },
  computed: {
    playVideoUrl() {
      const videoId = this.clickVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>