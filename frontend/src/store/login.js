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
            return Vue.http.post('api/auth/token/', credentials)
                .then(response => {
                    localStorage.setItem('accessToken', response.body.access)
                    localStorage.setItem('refreshToken', response.body.refresh)
                    commit('setErrors', {})

                    return response
                }).catch(err => {
                    commit('setErrors', err.body)
                    throw err
                })
        }
    }
}

export default login
