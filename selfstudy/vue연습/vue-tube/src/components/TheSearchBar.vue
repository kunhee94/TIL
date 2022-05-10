<template>
  <div>
    <input type="text"
    @keyup.enter="sendData">
  </div>
</template>

<script>
export default {
  name:'TheSearchVue',
  methods: {
    sendData(evnt){
      this.$emit('search', evnt.target.value)
    }
  }
}
</script>

<style>

</style>