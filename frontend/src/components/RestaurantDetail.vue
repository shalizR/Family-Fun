<template>
    <div v-if="restaurantDetail" class="container">
        <div class="columns">
            <div class="column is-6">
                <h1 class="title is-4 title_name">{{restaurantDetail.name}}</h1>
                <!--<h6>Price level:</h6>-->
                <!--<h6>Number of reviews</h6>-->
                <figure>
                    <img :src="$baseUrl + restaurantDetail.image" alt="restaurant_img">
                </figure>
                <div class="columns">
                    <div class="column">
                        <h2>{{restaurantDetail.street}}</h2>
                        <h2>{{restaurantDetail.ZIP}}, {{restaurantDetail.city}}</h2>
                        <h2>{{restaurantDetail.website}}</h2>
                        <h2>{{restaurantDetail.phone}}</h2>
                        <br>
                        <h2 v-if="restaurantDetail.kids_menu">Kids menu: Yes</h2>
                        <h2 v-else>Kids menu: No</h2>
                        <h2 v-if="restaurantDetail.take_reservation">Take reservation: Yes</h2>
                        <h2 v-else>Take reservation: No</h2>
                        <h2 v-if="restaurantDetail.credit_card">Accept credit cards: Yes</h2>
                        <h2 v-else>Accept credit cards: No</h2>
                        <!--<h2>Opening hours:</h2>-->
                        <!--<h2>{{restaurantDetail.opening_hours}}</h2>-->

                    </div>
                    <div class="column">
                        <lu-button class="add_button" v-on:click="navigateToNewReview(restaurantDetail)">Add a review</lu-button>
                    </div>
                </div>
            </div>
            <div class="column is-6">
                <h2 class="subtitle is-4 title_name">Reviews</h2>
                <div v-if="restaurantReviews">
                    <review-card v-for="review in restaurantReviews" :review="review"></review-card>
                </div>
                <div v-else>
                    No reviews yet!
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import {mapState} from 'vuex'
    import ReviewCard from "./ReviewCard";
    export default {
        components: {ReviewCard},
        beforeRouteUpdate(to, from, next) {
          this.$store.dispatch('restaurantDetail/fetchRestaurantDetail', this.id)
          this.$store.dispatch('restaurantDetail/fetchRestaurantReviews', this.id)
        },
        mounted() {
            this.$store.dispatch('restaurantDetail/fetchRestaurantDetail', this.id)
            this.$store.dispatch('restaurantDetail/fetchRestaurantReviews', this.id)
        },
        props: {
            id: [Number, String],
        },
        computed: {

            ...mapState('restaurantDetail', {
                restaurantDetail: (state) => state.restaurantDetail,
                restaurantReviews: (state) => state.restaurantReviews,

            })
        },
        // watch: {
        //     this.$store.dispatch('restaurantDetail/fetchRestaurantReviews', this.id)
        // },
        methods: {
            navigateToNewReview(restaurant) {
                this.$router.push({name: 'newReview', params: {id: restaurant.id}});

            }
        }
    }


</script>

<style lang="scss" scoped>
    @import "~bulma";

    .container {
        display: flex;
    }

    .title_name {
        text-decoration: underline;
        text-decoration-color: #e28a2b;
        text-decoration-style: solid;
    }
    .add_button {
        margin-left: 100px;
    }


</style>
