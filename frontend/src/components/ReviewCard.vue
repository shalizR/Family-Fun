<template>
<div class="card">
  <div class="card-content">
    <div class="media">
      <div class="media-left">
        <figure class="image is-48x48">
          <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
        </figure>
      </div>
      <div class="media-content">
        <p class="title is-4">{{ review.user.username }} rates {{ review.restaurant.name }} </p>
        <p class="subtitle is-6">Rating: {{ review.rating }}. Average Rating: {{ review.restaurant.rating }}</p>
      </div>
    </div>
    <div class="content">
      {{ review.content}}
    </div>
  </div>
</div>
</template>

<script>
export default {
  props: {
    review: {
      type: Object,
      required: true
    }
  }
}
</script>

<style lang="scss">
@import "~bulma";
</style>
