let baseUrl

if (process.env.NODE_ENV === 'development') {
    baseUrl = 'http://localhost:8000/backend/'
} else {
    baseUrl = 'http://family-fun.propulsion-learn.ch/backend/'
}
export {
    baseUrl
}