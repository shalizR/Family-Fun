const restaurantDetail = {
    namespaced: true,

    state: {
        restaurantDetail: {},
        restaurantReviews: {},
        newReview: {},
    },

    mutations: {
        setFetchedRestaurantDetail(state, payload) {
            console.log('detail', payload)
            state.restaurantDetail = payload
        },
        setFetchRestaurantReviews(state, payload) {
            console.log(payload)
            state.restaurantReviews = payload
        },
        setFetchNewReview(state, payload) {
            console.log(payload)
            state.newReview = payload
        },
        toggleHelpfulOpinion(state, {reviewId, opinionId}) {
            console.log('something')
            const opinion = state.restaurantReviews.find(d => d.id === reviewId)
                .opinions.find(d => d.id === opinionId)
            opinion.helpful = !opinion.helpful
        },
        toggleAwesomeOpinion(state, {reviewId, opinionId}) {
            const opinion = state.restaurantReviews.find(d => d.id === reviewId)
                .opinions.find(d => d.id === opinionId)
            opinion.awesome = !opinion.awesome
        },
        toggleRandomOpinion(state, {reviewId, opinionId}) {
            const opinion = state.restaurantReviews.find(d => d.id === reviewId)
                .opinions.find(d => d.id === opinionId)
            opinion.random = !opinion.random
        },
    },

    actions: {

        fetchRestaurantDetail(context, id) {
            const token = localStorage.getItem('accessToken')

            const myHeader = new Headers({
                Authorization: `Bearer ${token}`
            })
            console.log(id)
            const config = {
                method: 'GET',
                headers: myHeader
            }

            fetch(`http://localhost:8000/backend/api/restaurants/${id}/`, config)
                .then(res => res.json())
                .then((data) => {
                    context.commit('setFetchedRestaurantDetail', data)
                })
        },

        fetchRestaurantReviews(context, id) {
            const token = localStorage.getItem('accessToken')

            const myHeader = new Headers({
                Authorization: `Bearer ${token}`
            })
            const config = {
                method: 'GET',
                headers: myHeader,
            }

            fetch(`http://localhost:8000/backend/api/reviews/restaurant/${id}/`, config)
                .then(res => res.json())
                .then((data) => {
                    context.commit('setFetchRestaurantReviews', data)
                })

        },

        submitNewReview(context, params) {
            console.log('params', params)
            const token = localStorage.getItem('accessToken')
            const myHeader = new Headers({
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json'
            })

            const config = {
                method: 'POST',
                headers: myHeader,
                body: JSON.stringify(params.params),
            }

            console.log('config', config)

            fetch(`http://localhost:8000/backend/api/reviews/new/${params.id}/`, config)
                .then(res => res.json())
                .then(data => {
                    context.commit('setFetchNewReview', data)
                    console.log('data', data)
                })
        }


    }
}

export default restaurantDetail
