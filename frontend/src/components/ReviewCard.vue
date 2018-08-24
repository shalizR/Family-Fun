<template>
<div class="card">
  <div class="card-content" @click="handleReviewDetail">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img :src="$baseUrl + review.user.profile_pic" alt="user_image">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4">{{ review.user.username }}</p>
      </div>
    </div>
    <div class="content">
        <p class="subtitle is-6">{{review.content}}  {{ formatDate(this.review.date_created) }}</p>
        <p v-if="review.high_chair">Are there high chairs? Yes</p>
        <p v-else>Are there high chairs? No</p>
        <p v-if="review.are_there_steps">Are there steps? Yes</p>
        <p v-else>Are there steps: No</p>
        <p v-if="review.has_changing_table">Are there changing table for baby? Yes</p>
        <p v-else>Are there changing table for baby? No</p>
        <p v-if="place_for_stroller">Are there place for stroller? Yes</p>
        <p v-else>Are there place for stroller? No</p>
        <p v-if="isNoisy">Is there noisy? Yes</p>
        <p v-else>Is there noisy? No</p>
        <p v-if="friendly_waiting_staff">Are waiting Staff friendly? Yes</p>
        <p v-else>Are waiting Staff friendly? No</p>
        <p v-if="has_tablecloth">Have tables tablecloth? Yes</p>
        <p v-else>Have tables tablecloth? No</p>
        <p v-if="has_quick_service">Has quick service? Yes</p>
        <p v-else>Has quick service? No</p>

    </div>
  </div>
</div>
</template>

<script>
import moment from 'moment'

export default {

    data() {
        return {
            high_chair: false,
            are_there_steps: false,
            has_changing_table: false,
            place_for_stroller: false,
            isNoisy: false,
            friendly_waiting_staff: false,
            has_tablecloth: false,
            has_quick_service: false,

        }
    },
  props: {
    review: {
        type: Object,
        required: true,
        id: [Number, String]
    }
  },
    methods: {
        handleReviewDetail() {
            this.$router.push({ path: `/reviews/${this.review.id}`});
        },
        formatDate(date) {
            return moment(date).format('DD.MM.YYYY')
        }
    }
}
</script>

<style lang="scss">
@import "~bulma";
</style>


