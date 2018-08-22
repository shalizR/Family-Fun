import Vue from 'vue';
import Vuex from 'vuex';
// import restaurantDetail from './restaurantDetail';
import login from './login';
import search from './search';
import navbar from './navbar';
import validation from './validation';
import home from './home';

Vue.use(Vuex)

export default new Vuex.Store({
modules: {
    // restaurantDetail,
    login,
    search,
    navbar,
    validation,
    home,
},
});
