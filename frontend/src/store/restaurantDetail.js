const restaurantDetail = {
    namespaced: true,

    state: {
        restaurantDetail: {},
        restaurantReviews: {},
        newReview: {},
    },

    mutations: {
        setFetchedRestaurantDetail(state, payload) {
            state.restaurantDetail = payload
        },
        setFetchRestaurantReviews(state, payload) {
            state.restaurantReviews = payload
        },
        setFetchNewReview(state, payload) {
            state.newReview = payload
        },
        toggleHelpfulOpinion(state, {reviewId, opinionId}) {
            const review = state.restaurantReviews.find(d => d.id === reviewId)
            const opinion = review.opinions.find(d => d.id === opinionId)
            if (opinion) {
                opinion.helpful = !opinion.helpful
            } else {
                review.opinions.push({
                    id: opinionId,
                    helpful: true,
                    awesome: false,
                    random: false,
                })
            }
        },
        toggleAwesomeOpinion(state, {reviewId, opinionId}) {
            const review = state.restaurantReviews.find(d => d.id === reviewId)
            const opinion = review.opinions.find(d => d.id === opinionId)
            if (opinion) {
                opinion.awesome = !opinion.awesome
            } else {
                review.opinions.push({
                    id: opinionId,
                    helpful: false,
                    awesome: true,
                    random: false,
                })
            }
        },
        toggleRandomOpinion(state, {reviewId, opinionId}) {
            const review = state.restaurantReviews.find(d => d.id === reviewId)
            const opinion = review.opinions.find(d => d.id === opinionId)
            if (opinion) {
                opinion.random = !opinion.random
            } else {
                review.opinions.push({
                    id: opinionId,
                    helpful: false,
                    awesome: false,
                    random: true,
                })
            }
        },
    },

    actions: {

        fetchRestaurantDetail(context, id) {
            const token = localStorage.getItem('accessToken')

            const myHeader = new Headers({
                Authorization: `Bearer ${token}`
            })
            const config = {
                method: 'GET',
                headers: myHeader
            }

            return fetch(`http://localhost:8000/backend/api/restaurants/${id}/`, config)
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
            // in this way it waits until the fetch really happens
            return fetch(`http://localhost:8000/backend/api/reviews/restaurant/${id}/`, config)
                .then(res => res.json())
                .then((data) => {
                    context.commit('setFetchRestaurantReviews', data)
                })

        },

        submitNewReview(context, params) {
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

            return fetch(`http://localhost:8000/backend/api/reviews/new/${params.id}/`, config)
                .then(res => res.json())
                .then(data => {
                    context.commit('setFetchNewReview', data)
                })

        }


    }
}

export default restaurantDetail
