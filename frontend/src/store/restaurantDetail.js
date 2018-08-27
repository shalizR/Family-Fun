const restaurantDetail = {
  namespaced: true,

  state: {
    restaurantDetail: {},
    restaurantReviews: {},
  },

  mutations: {
    setFetchedRestaurantDetail (state, payload) {
      console.log(payload)
      state.restaurantDetail = payload
    },
    setFetchRestaurantReviews (state, payload){
        console.log(payload)
        state.restaurantReviews = payload
    }
  },

  actions: {

    fetchRestaurantDetail (context, id) {
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

    fetchRestaurantReviews (context, id) {
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

  }
}

export default restaurantDetail
