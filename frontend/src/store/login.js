import Vue from 'vue'

const login = {
    namespaced: true,

    state: {
        token: {},
        errors: {},
        userProfile: {},
    },

    mutations: {
        setToken(state, payload) {
            state.token = payload
        },
        setErrors(state, errors) {
            state.errors = errors
        },
        setUserProfile(state, userProfile) {
            state.userProfile = userProfile
        },
    },
    getters: {
        getErrors: state => state.errors,
        getUserProfile: state => state.userProfile,
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
        },
        fetchUserProfile: function ({commit}) {
            const token = localStorage.getItem('accessToken')
            if (token) {
                Vue.http.headers.common['Authorization'] = `Bearer ${token}`;
                return Vue.http.get('api/users/me/')
                    .then(response => {
                        commit('setUserProfile', response.body)
                        return response
                    }).catch(err => {
                        throw err
                    })


            }
        },
    }
}

export default login
