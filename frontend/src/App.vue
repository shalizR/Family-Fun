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
  },
  created() {
    this.$store.dispatch('login/fetchUserProfile')
  },
}
</script>

<style lang="scss">
#app {
  font-family: 'Varela Round', sans-serif;
}
  body {
    margin: 0;
    font-size: 100%;
  }
  a,p,address {
    font-size: 16px;
  }
  h1 {}
</style>
