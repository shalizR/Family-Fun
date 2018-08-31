<template>
    <div>
        <Search/>
        <div class="container">

            <div class='columns'>
                <div class="column is-4" v-for="restaurant in restaurants" v-bind:key="restaurant.id">
                    <restaurant-card :restaurant="restaurant"/>
                </div>
                <div v-if="!restaurants.length" class="column">Sorry, we couldn't find any content for search. Please try again!</div>
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
        props: ['search_text'],

        components: {
            Search,
            RestaurantCard
        },

        computed: {
            ...mapState('search', [
                'restaurants',
                'fast_foods',
                'cafes',
            ]),

        }
    }
</script>

<style lang="scss" scoped>
    @import "~bulma";

    * {
        box-sizing: border-box;
    }

    .columns {
        flex-wrap: wrap;
    }
</style>