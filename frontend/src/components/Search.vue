<template>
  <div class="container">
    <div class="select">
      <select v-model="category" v-on:click="renderCategory(category)">
        <option value="" disabled>Choose one...</option>
        <option v-for="category in categories" :value="category.key" v-bind:key="category.key">
          {{ category.name }}
        </option>
      </select>
    </div>
    <div class="control search-control">
      <input class="input" type="text" v-bind:placeholder="'Find ' + category"
             v-model="search_text">
    </div>
    <div>
      <lu-button @click="setSelectedSearch">Search</lu-button>
    </div>
</div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import RestaurantDetail from './RestaurantDetail'

export default {
  name: 'Search',
    data () {
    return {
      search_text: '',
      category: '',
    }
  },
  components: {
    // RestaurantDetail,
  },
  mounted () {
      this.$store.dispatch('search/fetchRestaurantCategories')
      console.log('this.categories[0]', this.categories[0])

      this.category = this.categories
      this.fetchRestaurants({ search_text: this.search_text, category: 'restaurant' });
  },
    updated () {
      console.log('this.categories[0]', this.category)
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
    setSelectedSearch: function() {
      this.fetchRestaurants({ search_text: this.search_text, category: this.category });
    },
    renderCategory: function (categoryName) {
        console.log('Clicked!', categoryName)
        this.category = categoryName
        this.fetchRestaurants({search_text: '', category: categoryName});
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
  }
  .search-control {
    width: 75%;
  }
  /*.dorpdown_color {*/
    /*color: #e28a2b;*/
  /*}*/
</style>
