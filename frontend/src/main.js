import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store'
import baseUrlPlugin from './plugins/baseUrl'
import Button from './components/Button'
import VueResource from 'vue-resource'
import {baseUrl} from "./store/constants";

//component registration in here
Vue.config.productionTip = false

Vue.use(VueResource)
Vue.use(baseUrlPlugin)
Vue.component('lu-button', Button)
Vue.http.options.root = baseUrl;
// Vue.http.headers.common['Authorization'] = 'Bearer <token>';

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
