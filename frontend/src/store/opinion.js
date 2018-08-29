const module = {
    namespaced: true,
    actions: {
        toggleHelpfulOpinion(context, data) {
            context.commit('restaurantDetail/toggleHelpfulOpinion', data, {root: true})
        },
        toggleAwesomeOpinion(context, data) {
            context.commit('restaurantDetail/toggleAwesomeOpinion', data, {root: true})
        },
        toggleRandomOpinion(context, data) {
            context.commit('restaurantDetail/toggleRandomOpinion', data, {root: true})
        },
    }
}

export default module












