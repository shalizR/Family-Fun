<template>
    <div class="container search-container">
        <div class="select">
            <select v-model="category" @change="renderCategory(category)">
                <option v-for="c in categories" :value="c" v-bind:key="c.key">
                    {{ c.name }}
                </option>
            </select>
        </div>
        <div class="control search-control">
            <input class="input" type="text" v-bind:placeholder="'Find ' + category.name"
                   v-model="search_text">
        </div>
        <div>
            <lu-button @click="setSelectedSearch">Search</lu-button>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: 'Search',
        data () {
            return {
                search_text: '',
                category: '',
            }
        },
        mounted () {
            this.$store.dispatch('search/fetchRestaurantCategories').then(o => {
                this.category = this.categories[0]
                this.fetchRestaurants({search_text: this.search_text, category: 'restaurant'});

            })
        },
        computed: {
            ...mapState('search', [
                'restaurants',
                'fast_foods',
                'cafes',
            ]),
            categories () {
                return this.$store.getters['search/getCategories'];
            },
        },
        methods: {
            setSelectedSearch: function () {
                this.fetchRestaurants({search_text: this.search_text, category: this.category.key});
            },
            renderCategory: function (category) {
                this.fetchRestaurants({search_text: '', category: category.key});
            },
            ...mapActions('search', [
                'fetchRestaurants',
                'fetchRestaurantCategories',
            ]),
        },
    };
</script>

<style lang="scss" scoped>
    @import "~bulma";

    .container {
        margin: 20px 0;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .search-control {
        width: 75%;
    }

    .search-container {
        margin: 20px auto;
    }

</style>
