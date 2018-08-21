<template>
  <div id="app">
    <div id="nav">
      <NavBar/>
    </div>
    <div class="container">
      <router-view/>
    </div>
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
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
