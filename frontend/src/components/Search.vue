<template>
  <div class="container">
    <div class="columns">
      <div class="column is-3">
        <div class="select">
          <select v-model="category" >
            <option v-for="category in categories" :value="category.key" v-bind:key="category.key">
              {{ category.name }}
            </option>
          </select>
        </div>
      </div>
      <div class="column is-6">
        <div class="control search-control">
          <input class="input" type="text" v-bind:placeholder="'Find ' + category"
                 v-model="search_text">
        </div>
      </div>
      <div class="column is-3">
        <div>
          <lu-button @click="setSelectedSearch">Search</lu-button>
        </div>

      </div>
    </div>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Search',
    data () {
    return {
      search_text: '',
      category: '',
    }
  },
  components: {
  },
  mounted () {
      this.$store.dispatch('search/fetchRestaurantCategories').then(data => {
          this.category = this.categories[0].key
      })
      this.fetchRestaurants({
          search_text: this.search_text,
      })
  },
  computed: {
    ...mapState('search', [
      'restaurants',
      'fast_foods',
      'cafes',
    ]),
    categories() {
      return this.$store.getters['search/getCategories'];
    },
  },
  methods: {
    setSelectedSearch() {
      this.fetchRestaurants({ search_text: this.search_text, category: this.category });
    },
    ...mapActions('search', [
      'fetchRestaurants',
      'fetchRestaurantCategories',
    ]),
  },
};
</script>

<style lang="scss">
@import "~bulma";

.search {
  display: flex;
  justify-content: center;
  width: 100%;
}
.search-control {
  width: 75%;
}
</style>
