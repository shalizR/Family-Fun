<template>
    <div class="container">
        <div class="columns">
            <div class="column is-11">
                <h1 class="title is-4">LOGIN</h1>
                <div class="errors" v-if="errors.non_field_errors">
                    {{errors.non_field_errors[0]}}
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3">
                <input required class="input" type="text" placeholder="Username" v-model="username">
                <div class="errors" v-if="errors.username">
                    {{errors.username[0]}}
                </div>
            </div>
            <div class="column is-3">
                <input required class="input " type="password" placeholder="Password" v-model="password">
                <div class="errors" v-if="errors.password">
                    {{errors.password[0]}}
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-6 button-container">
                <lu-button @click="handleLogin">Login</lu-button>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        data() {
            return {
                username: '',
                password: ''
            }
        },
        computed: {
            errors() {
                return this.$store.getters['login/getErrors']
            }
        },
        methods: {
            ...mapActions('login', [
                'fetchToken'
            ]),
            ...mapActions('navbar', [
                'setLoggedIn'
            ]),

            handleLogin() {
                this.fetchToken({
                    username: this.username,
                    password: this.password
                })
                .then(() => this.setLoggedIn(true))
                .then(() => {
                  this.$router.push({ name: 'home' })
                })
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import "../../node_modules/bulma";

    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%;
        font-family: 'Varela Round', sans-serif;
    }
    .button-container {
        display: flex;
        justify-content: center;
        justify-items: center;
    }
    .title {
        text-decoration: underline;
        text-decoration-color: #ffaf24;
        text-decoration-style: solid;
    }
    .errors {
    color: red;
    }
</style>
