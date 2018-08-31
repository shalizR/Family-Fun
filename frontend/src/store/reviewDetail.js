const reviewDetail = {
  namespaced: true,

  state: {
    reviewDetail: [], // convert to array
  },

  mutations: {
    setFetchedReviewDetail (state, payload) {
      state.reviewDetail = payload
    },

  },

  actions: {
    fetchReviewDetail (context, id) {
        const token = localStorage.getItem('accessToken')
        const myHeader = new Headers({
            Authorization: `Bearer ${token}`
        })
        const config = {
            method: 'GET',
            headers: myHeader,
        }

        return fetch(`http://localhost:8000/backend/api/reviews/${id}/`, config)
            .then(res => res.json())
            .then((data) => {
                context.commit('setFetchedReviewDetail', data)
            })
    },


  }
}

export default reviewDetail






