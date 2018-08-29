const search = {
    namespaced: true,

    state: {
        categories: [],
        restaurants: [],
        fast_foods: [],
        cafes: []
    },
    mutations: {
        setFetchedRestaurants(state, payload) {
            state.restaurants = payload
        },
        setFetchedRestaurantCategories(state, payload) {
            state.categories = payload
        }
    },

    actions: {
        fetchRestaurantCategories(context) {
            const token = localStorage.getItem('accessToken')
            const myHeader = new Headers({
                Authorization: `Bearer ${token}`,
            })

            const config = {
                method: 'GET',
                headers: myHeader
            }

            return fetch('http://localhost:8000/backend/api/restaurants/categories/', config)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    context.commit('setFetchedRestaurantCategories', data)
                })


        },
        fetchRestaurants(context, searchSettings) {
            if (!localStorage.getItem('accessToken')) {
                console.log('no token')
                return
            }
            const token = localStorage.getItem('accessToken')

            const myHeader = new Headers({
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json'
            })

            const config = {
                method: 'post',
                headers: myHeader,
            }
           return fetch(`http://localhost:8000/backend/api/search/${searchSettings.category}/?search_string=${searchSettings.search_text}`, config)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                        let restaurants = []
                        for (let restaurant of data) {
                            restaurants.push(restaurant)
                        }
                        context.commit('setFetchedRestaurants', restaurants)
                })
        }
    },
    getters: {
        getCategories(state) {
            return state.categories
        }
    }
}
export default search
