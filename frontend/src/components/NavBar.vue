// TODO: Show Login / Sign up / Logout Button depending on user logged in status

<template>
    <nav class="navbar nav-color" role="navigation">
        <div class="container">
            <div class="navbar-start">
                <h1 class="title">Family Fun</h1>
                <!--<figure class="navbar-item">-->
                <!--<img src="../assets/family_fun.jpg" @click="goToHome" alt="Family-fun logo">-->
                <!--</figure>-->
            </div>
            <div class="navbar-end">
                <router-link class="navbar-item" v-bind:to="{ name: 'home'}">Home</router-link>
                <!--<router-link class="navbar-item" v-bind:to="{ name: 'profile'}">Profile</router-link>-->
                <div class="navbar-item">
                    <router-link v-if="loginVisibility" class="button is-hovered" v-bind:to="{ name: 'login'}">Login
                    </router-link>
                    <a v-else-if="logoutVisibility" class="button" v-on:click="handleLogoutButton">Logout</a>
                </div>
            </div>

        </div>
    </nav>
</template>

<script>
    import {mapState, mapActions} from 'vuex'
    import Search from './Search.vue'

    export default {
        components: {
            Search,
        },
        computed: {
            ...mapState('navbar', [
                'logged_in'
            ]),
            loginVisibility() {
                return this.currentPath() !== '/login' && !this.logged_in
            },
            logoutVisibility() {
                return this.currentPath() !== '/login' && this.logged_in
            }
        },
        methods: {
            ...mapActions('navbar', [
                'setLoggedIn'
            ]),
            currentPath() {
                return this.$route.fullPath
            },
            handleLogoutButton() {
                this.setLoggedIn(false)
            },
            goToHome() {
                this.$router.push({name: 'home'})
            }
        },
        mounted() {
            if (localStorage.getItem('token') !== null) {
                this.setLoggedIn(true)
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import "~bulma";

    .navbar {
        margin-bottom: 25px;
        background-color: #ffaf24;
        /*color: white;*/

    }

    .navbar-start {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .navbar-item {
        color: white;
    }

    .title {
        color: white;
    }

</style>
