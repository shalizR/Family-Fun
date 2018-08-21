import Vue from "vue";

const validation = {
    namespaced: true,

    state: {
        token: {},
        errors: {},
    },

    mutations: {
        setToken(state, payload) {
            state.token = payload
        },
        setErrors(state, errors){
            state.errors = errors
        },
    },

    getters: {
        getErrors: state => state.errors
    },

    actions: {
        fetchToken: function (context, credentials) {
            const myHeader = new Headers({
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })

            // console.log(credentials.email, credentials.username, credentials.password, credentials.code, credentials.location)

            const config = {
                method: 'POST',
                headers: myHeader,
                body: JSON.stringify({
                    token: credentials.code,
                    username: credentials.username,
                    password: credentials.password,
                    location: credentials.location
                })
            }

            fetch('http://localhost:8000/backend/api/auth/registration/validation/', config)
                .then(res => res.json())
                .then((data) => {
                    console.log(data)
                })
        }
    }
}

export default validation

//     actions: {
//         fetchToken: function ({commit}, credentials) {
//             console.log(credentials)
//             return Vue.http.post('api/auth/token/', credentials).then(response => {
//                 console.log(response.body.access)
//                 console.log(response.body.refresh)
//                 localStorage.setItem('accessToken', response.body.access)
//                 localStorage.setItem('refreshToken', response.body.refresh)
//             }, response => {
//                 console.log("here", response)
//                 commit('setErrors', response.body)
//             });
//         }
//     }
// }
//
