<template>
    <div>
        <div class="card">
            <div class="card-content" @click="handleRestaurantDetail">
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
                <div class="content">
                    <div class="columns">
                        <div class="column is-6">
                            <p class="subtitle is-6">{{restaurant.street}}{{restaurant.ZIP}}, {{restaurant.city}}</p>
                            <p class="subtitle is-6">{{restaurant.phone}}</p>
                            <p class="subtitle is-6">{{restaurant.website}}</p>
                        </div>
                        <div class="column is-6">
                            <p v-if="restaurant.kids_menu">Kids menu: Yes</p>
                            <p v-else>Kids menu: No</p>
                            <p v-if="restaurant.take_reservation">Take reservation: Yes</p>
                            <p v-else>Take reservation: No</p>
                            <p v-if="restaurant.credit_card">Accept credit cards: Yes</p>
                            <p v-else>Accept credit cards: No</p>
                        </div>
                    </div>
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

</style>


