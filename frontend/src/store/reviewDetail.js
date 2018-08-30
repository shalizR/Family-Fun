const reviewDetail = {
  namespaced: true,

  state: {
    reviewDetail: [], // convert to array
  },

  mutations: {
    setFetchedReviewDetail (state, payload) {
      state.reviewDetail = payload
    },
    setFetchedDeleteReview(state, payload) {
        const review = state.reviewDetail.find(o => o.id === payload.reviewId)
        const index = state.reviewDetail.indexOf(review)
        state.reviewDetail.splice(index, 1)
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

    deleteReview(context, id) {
        const token = localStorage.getItem('accessToken')
        const myHeader = new Headers({
            Authorization: `Bearer ${token}`
        })
        const config = {
            method: 'DELETE',
            headers: myHeader,
        }
        return fetch(`http://localhost:8000/backend/api/reviews/${id.reviewId}/`, config)
            .then(res => {
                if(res.status === 204) {
                    context.commit('setFetchedDeleteReview', id)
                }
                else {
                    return res
                }
            })
    },


  }
}

export default reviewDetail






