import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Validation from './components/Validation';

Vue.use(Router);

export default new Router({
  routes: [
    // {
    //   path: '/restaurants/:id/',
    //   name: 'RestaurantDetail',
    //   component: RestaurantDetail
    // },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    // {
    //   path: '/search',
    //   name: 'search',
    //   component: Search
    // },
    // {
    //   path: '/profile',
    //   name: 'profile',
    //   component: Profile
    // },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    // {
    //   path: '/footer',
    //   name: 'footer',
    //   component: Footer
    // },
    {
      path: '/validation',
      name: 'validation',
      component: Validation
    }
  ]
});
