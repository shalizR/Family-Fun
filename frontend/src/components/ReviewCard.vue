<template>
    <div class="card">
        <div class="card-content">
            <div class="media">
                <div class="media-left">
                    <figure class="image is-48x48 user_pic">
                        <img :src="$baseUrl + review.user.profile_pic" alt="user_image" class="review-image">
                    </figure>
                </div>
                <div class="media-content">
                    <p class="title is-4">{{ review.user.username }}</p>
                    <p class="subtitle">"{{review.content}}" {{ formatDate(this.review.date_created) }}</p>
                </div>
            </div>
            <div class="columns">
                <div class="column">
                    <h3 v-if="review.high_chair">High chairs? <strong>Yes</strong></h3>
                    <h3 v-else>High chairs? <strong>No</strong></h3>
                    <h3 v-if="review.are_there_steps">Steps? <strong>Yes</strong></h3>
                    <h3 v-else>Steps? <strong>No</strong></h3>
                    <h3 v-if="review.has_changing_table">Changing table for babies? <strong>Yes</strong></h3>
                    <h3 v-else>Changing table for babies? <strong>No</strong></h3>
                    <h3 v-if="review.has_quick_service">Quick service? <strong>Yes</strong></h3>
                    <h3 v-else>Quick service? No</h3>
                </div>
                <div class="column">
                    <h3 v-if="review.place_for_stroller">Place for stroller? <strong>Yes</strong></h3>
                    <h3 v-else>Place for stroller? <strong>No</strong></h3>
                    <h3 v-if="review.isNoisy">Noisy? <strong>Yes</strong></h3>
                    <h3 v-else>Noisy: <strong>No</strong></h3>
                    <h3 v-if="review.friendly_waiting_staff">Friendly waiting staff? <strong>Yes</strong></h3>
                    <h3 v-else>Friendly waiting staff? <strong>No</strong></h3>
                    <h3 v-if="review.has_tablecloth">Has tablecloth? <strong>Yes</strong></h3>
                    <h3 v-else>Has tablecloth: <strong>No</strong></h3>
                </div>
            </div>

            <div class="columns">
                <div class="column container">
                    <div class="item1">
                        <div v-if="!checkUserDelete">
                            <div class="label">Was this review ...?</div>
                            <div class="grouped-button">
                                <lu-button v-on:click="toggleHelpfulOpinion">Helpful {{helpfulCounter}}</lu-button>
                                <lu-button v-on:click="toggleAwesomeOpinion">Awesome {{awesomeCounter}}</lu-button>
                                <lu-button v-on:click="toggleRandomOpinion">Random {{randomCounter}}</lu-button>
                            </div>

                        </div>
                    </div>
                    <div class="item2">
                        <lu-button v-if="checkUserDelete" @click="handleDelete" class="is-danger">Delete review</lu-button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import moment from 'moment';

    export default {

        props: {
            review: {
                type: Object,
                required: true,
                id: [Number, String]
            }
        },
        computed: {
            checkUserDelete() {
                return this.$store.getters['login/getUserProfile'] && this.$store.getters['login/getUserProfile'].id === this.review.user.id
            },
            helpfulCounter() {
                return this.review.opinions.filter(o => o.helpful === true).length
            },
            awesomeCounter() {
                return this.review.opinions.filter(o => o.awesome === true).length
            },
            randomCounter() {
                return this.review.opinions.filter(o => o.random === true).length
            },
        },
        methods: {
            formatDate(date) {
                return moment(date).format('DD/MM/YYYY')
            },
            handleDelete() {
                this.$store.dispatch('restaurantDetail/deleteReview', this.review.id)
            },

            toggleHelpfulOpinion() {
                const token = localStorage.getItem('accessToken')
                const myHeader = new Headers({
                    Authorization: `Bearer ${token}`
                })
                const config = {
                    method: 'GET',
                    headers: myHeader,
                }

                return fetch(`${this.$baseUrl}/api/opinions/helpful/${this.review.id}/`, config)
                    .then(res => res.json())
                    .then((data) => {
                        this.$store.dispatch('opinion/toggleHelpfulOpinion', {
                            opinionId: data.id,
                            reviewId: this.review.id
                        })
                    })
            },
            toggleAwesomeOpinion() {
                const token = localStorage.getItem('accessToken')
                const myHeader = new Headers({
                    Authorization: `Bearer ${token}`
                })
                const config = {
                    method: 'GET',
                    headers: myHeader,
                }

                return fetch(`${this.$baseUrl}/api/opinions/awesome/${this.review.id}/`, config)
                    .then(res => res.json())
                    .then((data) => {
                        this.$store.dispatch('opinion/toggleAwesomeOpinion', {
                            opinionId: data.id,
                            reviewId: this.review.id
                        })
                    })
            },
            toggleRandomOpinion() {
                const token = localStorage.getItem('accessToken')
                const myHeader = new Headers({
                    Authorization: `Bearer ${token}`
                })
                const config = {
                    method: 'GET',
                    headers: myHeader,
                }

                return fetch(`${this.$baseUrl}/api/opinions/random/${this.review.id}/`, config)
                    .then(res => res.json())
                    .then((data) => {
                        this.$store.dispatch('opinion/toggleRandomOpinion', {
                            opinionId: data.id,
                            reviewId: this.review.id
                        })
                    })
            },
        },


    }
</script>

<style lang="scss" scoped>
    @import "~bulma";

    .container {
        display: flex;
        width: 100%;
        justify-content: space-between;
    }

    .item1 {
        display: flex;
        flex-direction: column;
    }

    .item2 {
        align-self: flex-end;
    }

    .user_pic {
        height: 100% !important;
        width: auto !important;
    }

    .grouped-button {
        display: flex;
        justify-content: space-between;
        width: 321px;
    }
    strong{
        float: right;
    }
    h3 {
        border-bottom: 1px solid #ededed;
        &:first-child {
                    border-top: 1px solid #ededed;

        }
    }

    .review-image {
        width: 70px !important;
        height: 70px !important;
    }
</style>


