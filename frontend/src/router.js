import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import RestaurantDetail from './components/RestaurantDetail';
import NewReview from './components/NewReview';

Vue.use(Router); //it's global like this

export default new Router({
    routes: [
        {
            path: '/restaurants/:id/',
            name: 'RestaurantDetail',
            props: true,
            component: RestaurantDetail
        },
        {
            path: '/',
            name: 'home',
            component: Home
        },
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
            path: '/newreview/:id/',
            name: 'newReview',
            component: NewReview,
            props: true,

        }

    ]
});
