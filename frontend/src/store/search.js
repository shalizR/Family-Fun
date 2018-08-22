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
          console.log(payload)
            state.categories = payload
        }
    },
    actions: {
        fetchRestaurantCategories(context) {
            if (!localStorage.getItem('accessToken')) {
                return
            }
            const parsedToken = localStorage.getItem('accessToken')
            const myHeader = new Headers({
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${parsedToken}`,
            })

            const config = {
                method: 'GET',
                headers: myHeader
            }

            fetch('http://localhost:8000/backend/api/restaurants/categories/', config)
                .then(response => {
                    console.log(response)
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
            const parsedToken = localStorage.getItem('accessToken')

            const myHeader = new Headers({
                'Authorization': `Bearer ${parsedToken}`,
                'Content-Type': 'application/json'
            })

            const config = {
                method: 'post',
                headers: myHeader,
            }
            fetch(`http://localhost:8000/backend/api/search/${searchSettings.category}/?search_string=${searchSettings.search_text}`, config)
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
