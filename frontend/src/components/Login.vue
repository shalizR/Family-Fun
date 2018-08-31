<template>
    <div class="login-container">
        <div>
            <h1 class="title is-4">LOGIN</h1>
            <div class="errors" v-if="errors.non_field_errors">
                {{errors.non_field_errors[0]}}
            </div>
        </div>
        <div class="login-inputs">
            <div>
                <input required class="input" type="text" placeholder="Username" v-model="username">
                <div class="errors" v-if="errors.username">
                    {{errors.username[0]}}
                </div>
            </div>
            <div>
                <input required class="input " type="password" placeholder="Password" v-model="password">
                <div class="errors" v-if="errors.password">
                    {{errors.password[0]}}
                </div>
            </div>
        </div>
        <div class="button-container">
            <lu-button class="button-login" @click="handleLogin">Login</lu-button>
        </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex'

    export default {
        data () {
            return {
                username: '',
                password: ''
            }
        },
        computed: {
            errors () {
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

            handleLogin () {
                this.fetchToken({
                    username: this.username,
                    password: this.password
                })
                    .then(() => this.setLoggedIn(true))
                    .then(() => {
                        this.$router.push({name: 'home'})
                    })
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import "../../node_modules/bulma";

    .login-container {
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
        font-family: 'Varela Round', sans-serif;
        height: 300px;
        width: 500px;
        margin: 0 auto;
    }

    .login-inputs {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100px;

    }

    .button-container {
        display: flex;
        justify-content: space-between;
    }

    .button-login {
        padding: 0 20px;
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
