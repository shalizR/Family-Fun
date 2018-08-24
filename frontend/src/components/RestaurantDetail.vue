<template>
  <div v-if="restaurantDetail" id="main_container">
    <div class="columns">
      <div class="column is-6 is-offset-3">
        <h1 class="title is-4">{{restaurantDetail.name}}</h1>
        <h6>Price level:</h6>
        <h6>Number of reviews</h6>

      </div>
    </div>
    <div class="columns">
      <div class="column is-6 is-offset-3">
        <figure>
          <img :src="$baseUrl + restaurantDetail.image" alt="restaurant_img">
        </figure>
      </div>
      <div class="column is-6">
        <!--<input required class="input  is-medium" type="password" placeholder="Password" v-model="password">-->
        <h2>{{restaurantDetail.street}}</h2>
        <h2>{{restaurantDetail.ZIP}}, {{restaurantDetail.city}}</h2>
        <h2>{{restaurantDetail.website}}</h2>
        <h2>{{restaurantDetail.phone}}</h2>
        <h2 v-if="restaurantDetail.kids_menu">Kids menu: Yes</h2>
        <h2 v-else>Kids menu: No</h2>
        <h2 v-if="restaurantDetail.take_reservation">Take reservation: Yes</h2>
        <h2 v-else>Take reservation: No</h2>
        <h2 v-if="restaurantDetail.credit_card">Accept credit cards: Yes</h2>
        <h2 v-else>Accept credit cards: No</h2>
        <p>Opening hours:</p>

      </div>
    </div>
    <div class="columns">
      <div class="column is-6 is-offset-3 button-container">
        <lu-button>Search in reviews ... </lu-button>
      </div>
    </div>
    <div class="columns">
      <div class="column is-6 is-offset-3 button-container">
        <lu-button>Add a review</lu-button>
      </div>
    </div>


    <div  id="review_container">
      <div v-if="restaurantReviews">
        <review-card v-for="review in restaurantReviews" :review="review"></review-card>
      </div>
    </div>
  </div>
</template>
<script>
import {mapState, mapActions} from 'vuex'
import ReviewCard from "./ReviewCard";


export default {
    components: {ReviewCard},
    beforeRouteUpdate (to, from, next) {
      this.$store.dispatch('restaurantDetail/fetchRestaurantDetail', this.id)
      this.$store.dispatch('restaurantDetail/fetchRestaurantReviews', this.id)
  },
  created () {
      console.log(this.id)
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
    // handleNewReview () {
    //
    // }
  }
}

</script>

<style lang="scss">
  @import "~bulma";

</style>
