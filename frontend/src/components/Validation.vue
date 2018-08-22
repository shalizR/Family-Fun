<template>
  <div>
    <div class="columns">
      <div class="column is-6 is-offset-3">
        <h1 class="title is-4">VERIFICATION</h1>
      </div>
    </div>
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <input required class="input  is-medium" type="text" placeholder="E-Mail address" v-model="email">
      </div>
      <div class="column is-3">
        <input required class="input is-medium" type="text" placeholder="Validation code" v-model="code">
      </div>
    </div>
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <input required class="input  is-medium" type="text" placeholder="Username" v-model="username">
      </div>
      <div class="column is-3">
        <input required class="input  is-medium" type="text" placeholder="Location" v-model="location">
      </div>
    </div>
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <input required class="input  is-medium" type="password" placeholder="Password" v-model="password">
      </div>
      <div class="column is-3">
        <p v-if="password_error">Passwords do not match!!!</p>
        <input required class="input  is-medium" type="password" placeholder="Password repeat"
               v-model="password_repeat">
      </div>
    </div>
    <div class="columns">
      <div class="column is-6 is-offset-3 button-container">
        <lu-button @click="handleValidation">Finish registration</lu-button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  data () {
    return {
      email: '',
      username: '',
      password: '',
      code: '',
      location: '',
      password_repeat: '',
      password_error: false
    }
  },
  methods: {
    ...mapActions('validation', [
      'fetchToken'
    ]),

    handleValidation () {
      if (this.password !== this.password_repeat) {
        this.password_error = true
      } else {
        this.password_error = false
        this.fetchToken({
          email: this.email,
          username: this.username,
          password: this.password,
          code: this.code,
          location: this.location
        })
      }
    }
  }
}
</script>

<style scoped>
  @import "../../node_modules/bulma";

  .button-container {
    display: flex;
    justify-content: center;
  }
    .title{
    text-decoration:underline;
    text-decoration-color: #e28a2b;
    text-decoration-style: solid;
  }

</style>
