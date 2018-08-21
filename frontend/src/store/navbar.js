const navbar = {
  namespaced: true,

  state: {
    logged_in: false
  },
  mutations: {
    setLoggedIn (state, loggedIn) {
      if (!loggedIn) {
        localStorage.removeItem('token')
      }
      state.logged_in = loggedIn
    }
  },
  actions: {
    setLoggedIn (context, loggedIn) {
      context.commit('setLoggedIn', loggedIn)
    }
  }
}

export default navbar
