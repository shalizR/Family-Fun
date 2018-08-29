<template>
  <div id="app">
    <div id="nav">
      <NavBar/>
    </div>
      <router-view/>
    <!--<div>-->
      <!--<Footer/>-->
    <!--</div>-->
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
// import Footer from './components/Footer.vue'

export default {
  components: {
    NavBar,
    // Footer
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Varela Round', sans-serif;
}
</style>
