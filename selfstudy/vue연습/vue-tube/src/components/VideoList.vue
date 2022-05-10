<template>
  <div>
    <video-list-item v-for="(video, idx) in videos" :key=idx
      :video="video"
      @send-data="sendData"></video-list-item>

  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos:Array,
  },
  methods: {
    sendData(data){
      this.$emit('pick-video', data)
    }
  }
}
</script>

<style>

</style>