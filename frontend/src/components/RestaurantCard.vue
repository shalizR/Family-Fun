<template>
<div class="card">
  <div class="card-content" @click="handleRestaurantDetail">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img :src="$baseUrl + restaurant.image" alt="restaurant_img">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4">{{ restaurant.name }}</p>
        <p class="subtitle is-6">Rating: {{ Math.round(restaurant.rating) }} </p>
      </div>
    </div>
    <div class="content">
        <p class="subtitle is-6">{{restaurant.street}}</p>
        <p class="subtitle is-6">{{restaurant.ZIP}}</p>
        <p class="subtitle is-6">{{restaurant.city}}</p>
        <p class="subtitle is-6">{{restaurant.phone}}</p>
        <!--&lt;!&ndash;<p>{{restaurantDetail.opening_hours}}</p>&ndash;&gt;-->
        <p v-if="restaurant.kids_menu">Kids menu: Yes</p>
        <p v-else>Kids menu: No</p>
        <p v-if="restaurant.take_reservation">Take reservation: Yes</p>
        <p v-else>Take reservation: No</p>
        <p v-if="restaurant.credit_card">Accept credit cards: Yes</p>
        <p v-else>Accept credit cards: No</p>
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
            this.$router.push({ path: `/restaurants/${this.restaurant.id}`});
        }
    }
}
</script>

<style lang="scss">
@import "~bulma";
</style>


