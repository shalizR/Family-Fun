function install (Vue) {
  // 4. add an instance method
  if (process.env.NODE_ENV === 'development') {
    Vue.prototype.$baseUrl = 'http://localhost:8080/backend'
  } else {
    Vue.prototype.$baseUrl = 'http://family-fun.propulsion-learn.ch/backend'
  }
}

export default install
