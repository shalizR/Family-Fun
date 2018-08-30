import Vue from 'vue';
import Vuex from 'vuex';
import login from './login';
import search from './search';
import navbar from './navbar';
import home from './home';
import opinion from './opinion';
import restaurantDetail from './restaurantDetail';
import reviewDetail from './reviewDetail';

Vue.use(Vuex)

export default new Vuex.Store({
modules: {
    login,
    search,
    navbar,
    home,
    restaurantDetail,
    opinion,
    reviewDetail,
},
});
