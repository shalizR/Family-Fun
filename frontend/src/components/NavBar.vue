// TODO: Show Login / Sign up / Logout Button depending on user logged in status

<template>
<nav class="navbar is-primary" role="navigation">
    <div class="navbar-start">
      <figure class="navbar-item image">
        <img src="../assets/family_fun_small.png" width="112" height="28" alt="Family-fun logo">
      </figure>
    </div>
    <div class="navbar-end">
      <router-link class="navbar-item" v-bind:to="{ name: 'home'}">Home</router-link>
      <router-link class="navbar-item" v-bind:to="{ name: 'search'}">Search</router-link>
      <router-link class="navbar-item" v-bind:to="{ name: 'profile'}">Profile</router-link>
      <div class="navbar-item">
        <router-link v-if="loginVisibility" class="button" v-bind:to="{ name: 'login'}">Login</router-link>
        <a v-else-if="logoutVisibility" class="button" v-on:click="handleLogoutButton">Logout</a>
      </div>
  </div>
</nav>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Search from './Search.vue'

export default {
    components: {
        Search,
    },
  computed: {
    ...mapState('navbar', [
      'logged_in'
    ]),
    loginVisibility () {
      return this.currentPath() !== '/login' && !this.logged_in
    },
    logoutVisibility () {
      return this.currentPath() !== '/login' && this.logged_in
    }
  },
  methods: {
    ...mapActions('navbar', [
      'setLoggedIn'
    ]),
    currentPath () {
      return this.$route.fullPath
    },
    handleLogoutButton () {
      this.setLoggedIn(false)
    }
  },
  mounted () {
    if (localStorage.getItem('token') !== null) {
      this.setLoggedIn(true)
    }
  }
}
</script>

<style lang="scss">
@import "~bulma";
    .nav-color {
        background-color: yellow;
    }
</style>
