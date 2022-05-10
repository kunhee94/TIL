<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">

    <video-detail 
    :clickVideo="clickVideo"></video-detail>

    <the-search-bar @search="searchData"></the-search-bar>

    <video-list :videos="videos"
    @pick-video="pickVideo"></video-list>

  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      videos: [],
      clickVideo: null,
    }
  },
  methods: {
    searchData(keyword){
      console.log(keyword)
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const API_KEY = 'AIzaSyAmCiwBXQvB4HMH-zSJvWxe7Qe5nwhvIoo'
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          q:keyword,
          type:'video',
        }
      })
        .then(res=>{
          this.videos = res.data.items
        })
    },
    pickVideo(data){
      this.clickVideo = data
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
