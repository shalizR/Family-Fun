<template>
    <div class="container">
        <div>
            Hello!!!!!!
        </div>
        <Search/>
        <div class='columns is-multiline is-centered'>
            <div class="column is-4" v-for="restaurant in restaurants" v-bind:key="restaurant.id">
                <restaurant-card :restaurant="restaurant"/>
            </div>
        </div>
    </div>
</template>

<script>
    import RestaurantCard from './RestaurantCard'
    import {mapState} from 'vuex'
    import search from './Search.vue'
    import Search from "./Search";

    export default {
        components: {
            Search,
            RestaurantCard},

        computed: {
            ...mapState('search', [
                'restaurants',
                'fast_foods',
                'cafes',
            ]),

        }
    }
</script>

<style scoped>
    @import "../../node_modules/bulma";

</style>