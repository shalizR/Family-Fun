import Vue from 'vue'
const login = {
    namespaced: true,

    state: {
        token: {},
        errors: {}
    },

    mutations: {
        setToken(state, payload) {
            state.token = payload
        },
        setErrors (state, errors) {
            state.errors = errors
        }
    },
    getters: {
        getErrors: state => state.errors
    },
    actions: {
        fetchToken: function ({commit}, credentials) {
            console.log(credentials)
            return Vue.http.post('api/auth/token/', credentials).then(response => {
                console.log(response.body.access)
                console.log(response.body.refresh)
                localStorage.setItem('accessToken', response.body.access)
                localStorage.setItem('refreshToken', response.body.refresh)
            }, response => {
                console.log("here", response)
                commit('setErrors', response.body)
            });
        }
    }
}

export default login
