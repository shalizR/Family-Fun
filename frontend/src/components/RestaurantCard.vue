<template>
        <div class="card"  @click="handleRestaurantDetail">
                <div class="media">
                    <div class="media-left">
                        <figure class="image is-64x64">
                            <img :src="$baseUrl + restaurant.image" alt="restaurant_img">
                        </figure>
                    </div>
                    <div class="media-content">
                        <h2 class="title is-4">{{ restaurant.name }}</h2>
                        <h3 class="subtitle is-6">Rating: {{ Math.round(restaurant.rating) }} </h3>
                    </div>
                </div>
                <div class="content content-container">
                    <div class="columns">
                        <!--<div class="column">-->
                            <!--<p class="subtitle is-6">{{restaurant.street}}{{restaurant.ZIP}}, {{restaurant.city}}</p>-->
                            <!--<p class="subtitle is-6">{{restaurant.phone}}</p>-->
                            <!--<p class="subtitle is-6">{{restaurant.website}}</p>-->
                        <!--</div>-->
                        <div class="column">
                            <p v-if="restaurant.kids_menu">Kids menu: <strong>Yes</strong></p>
                            <p v-else>Kids menu: <strong>No</strong></p>
                            <p v-if="restaurant.take_reservation">Take reservation: <strong>Yes</strong></p>
                            <p v-else>Take reservation: <strong>No</strong></p>
                            <p v-if="restaurant.credit_card">Accept credit cards: <strong>Yes</strong></p>
                            <p v-else>Accept credit cards: <strong>No</strong></p>
                        </div>
                    </div>
                </div>
        </div>
</template>

<script>

    export default {
        props: {
            restaurant: {
                type: Object,
                required: true,
                id: [Number, String]
            }
        },
        methods: {
            handleRestaurantDetail() {
                this.$router.push({path: `/restaurants/${this.restaurant.id}`, props: this.restaurant.id});
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import "~bulma";

    p {
        margin: 0 !important;
    }
    img {
        height: 100% !important;
        width: auto !important;
    }

    .card {
        margin-bottom: 20px;
        padding: 10px;
    }

    .content-container {
        /*display: flex;*/
    }

</style>


