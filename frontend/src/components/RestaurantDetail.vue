<template>
    <div v-if="restaurantDetail" class="container">
        <div class="columns">
            <div class="column is-6">
                <h1 class="title title_name">{{restaurantDetail.name}}</h1>
                <!--<h6>Price level:</h6>-->
                <!--<h6>Number of reviews</h6>-->
                <figure>
                    <img :src="$baseUrl + restaurantDetail.image" alt="restaurant_img">
                </figure>
                <div class="columns">
                    <div class="column is-8">
                        <address>
                            {{restaurantDetail.name}}<br>
                            {{restaurantDetail.street}}<br>
                            {{restaurantDetail.ZIP}}, {{restaurantDetail.city}}<br>

                        </address>
                        <ul>
                            <li>
                                <a :href="restaurantDetail.website" target="_blank"
                                   v-text="restaurantDetail.website"></a>
                            </li>
                            <li>
                                <a :href="`tel:${restaurantDetail.phone}`" target="_blank"
                                   v-text="restaurantDetail.phone"></a>
                            </li>
                        </ul>
                        <br>
                        <p v-if="restaurantDetail.kids_menu">strongKids menu: <strong>Yes</strong></p>
                        <p v-else>Kids menu: <strong>No</strong></p>
                        <p v-if="restaurantDetail.take_reservation">Take reservation: <strong>Yes</strong></p>
                        <p v-else>Take reservation: <strong>No</strong></p>
                        <p v-if="restaurantDetail.credit_card">Accept credit cards: <strong>Yes</strong></p>
                        <p v-else>Accept credit cards: <strong>No</strong></p>
                        <!--<h2>Opening hours:</h2>-->
                        <!--<h2>{{restaurantDetail.opening_hours}}</h2>-->

                    </div>
                    <div class="column is-3 button-box">
                        <lu-button class="add_button" v-on:click="navigateToNewReview(restaurantDetail)">Add a review
                        </lu-button>
                    </div>
                </div>
            </div>
            <div class="column is-6 review-scrollbar">
                <h2 class="subtitle title_name">Reviews</h2>
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
        methods: {
            navigateToNewReview(restaurant) {
                this.$router.push({name: 'newReview', params: {id: restaurant.id}});

            }
        }
    }


</script>

<style lang="scss" scoped>
    @import "~bulma";

    .title_name {
        text-decoration: underline;
        text-decoration-color: #e28a2b;
        text-decoration-style: solid;
    }

    .button-box {
        text-align: right;
        padding: 20px;
    }
    .review-scrollbar {
        overflow-y: auto;
        max-height: calc(100vh - 190px);

    }
</style>
