import Vue from 'vue';
import Vuex from 'vuex';
import login from './login';
import search from './search';
import navbar from './navbar';
import validation from './validation';
import home from './home';
import opinion from './opinion';
import restaurantDetail from './restaurantDetail'

Vue.use(Vuex)

export default new Vuex.Store({
modules: {
    login,
    search,
    navbar,
    validation,
    home,
    restaurantDetail,
    opinion,
},
});
