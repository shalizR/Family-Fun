import {baseUrl} from "../store/constants";

function install (Vue) {
    Vue.prototype.$baseUrl = baseUrl
}

export default install
