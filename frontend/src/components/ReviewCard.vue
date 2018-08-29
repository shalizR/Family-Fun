<template>
    <div class="card">
        <div class="card-content">
            <div class="media">
                <div class="media-left">
                    <figure class="image is-48x48 user_pic">
                        <img :src="$baseUrl + review.user.profile_pic" alt="user_image">
                    </figure>
                </div>
                <div class="media-content">
                    <p class="title is-4">{{ review.user.username }}</p>
                    <p class="subtitle">"{{review.content}}" {{ formatDate(this.review.date_created) }}</p>
                </div>
            </div>
            <div class="columns">
                <div class="column">
                    <h3 v-if="high_chair">High chairs? Yes</h3>
                    <h3 v-else-if="!high_chair">High chairs? No</h3>
                    <h3 v-else>High chairs? None</h3>
                    <h3 v-if="are_there_steps">Steps? Yes</h3>
                    <h3 v-else-if="!are_there_steps">Steps? No</h3>
                    <h3 v-else>Steps: None</h3>
                    <h3 v-if="has_changing_table">Changing table for babies? Yes</h3>
                    <h3 v-else-if="!has_changing_table">Changing table for babies? No</h3>
                    <h3 v-else>Changing table for baby? None</h3>
                    <h3 v-if="has_quick_service">Quick service? Yes</h3>
                    <h3 v-else-if="!has_quick_service">Quick service? No</h3>
                    <h3 v-else>Quick service: None</h3>
                </div>
                <div class="column">
                    <h3 v-if="place_for_stroller">Place for stroller? Yes</h3>
                    <h3 v-else-if="!place_for_stroller">Place for stroller? No</h3>
                    <h3 v-else>Place for stroller? None</h3>
                    <h3 v-if="isNoisy">Noisy? Yes</h3>
                    <h3 v-else-if="!isNoisy">Noisy: No</h3>
                    <h3 v-else>Noisy: None</h3>
                    <h3 v-if="friendly_waiting_staff">Friendly waiting staff? Yes</h3>
                    <h3 v-else-if="!friendly_waiting_staff">Friendly waiting staff? No</h3>
                    <h3 v-else>Friendly waiting staff? None</h3>
                    <h3 v-if="has_tablecloth">Has tablecloth? Yes</h3>
                    <h3 v-else-if="!has_tablecloth">Has tablecloth: No</h3>
                    <h3 v-else>Has tablecloth: None</h3>
                </div>
            </div>
            <div class="columns">
                <div class="column">
                    <p>Was this review ...?</p>
                    <lu-button v-on:click="toggleHelpfulOpinion">Helpful {{helpfulCounter}}</lu-button>
                    <lu-button v-on:click="toggleAwesomeOpinion">Awesome {{awesomeCounter}}</lu-button>
                    <lu-button v-on:click="toggleRandomOpinion">Random {{randomCounter}}</lu-button>
                </div>

            </div>


        </div>
    </div>
</template>

<script>
    import moment from 'moment'

    export default {

        data() {
            return {
                high_chair: false,
                are_there_steps: false,
                has_changing_table: false,
                place_for_stroller: false,
                isNoisy: false,
                friendly_waiting_staff: false,
                has_tablecloth: false,
                has_quick_service: false,

            }
        },
        props: {
            review: {
                type: Object,
                required: true,
                id: [Number, String]
            }
        },
        computed: {
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
        // to see the changes immediately
        mounted() {
            this.$store.dispatch('opinion/toggleHelpfulOpinion', {opinionId:data.id, reviewId:this.review.id})
            this.$store.dispatch('opinion/toggleAwesomeOpinion', {opinionId:data.id, reviewId:this.review.id})
            this.$store.dispatch('opinion/toggleRandomOpinion', {opinionId:data.id, reviewId:this.review.id})
        },


        methods: {
            formatDate(date) {
                return moment(date).format('DD/MM/YYYY')
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

                fetch(`${this.$baseUrl}/api/opinions/helpful/${this.review.id}/`, config)
                    .then(res => res.json())
                    .then((data) => {
                        console.log('data', data)
                        this.$store.dispatch('opinion/toggleHelpfulOpinion', {opinionId:data.id, reviewId:this.review.id})
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

                fetch(`${this.$baseUrl}/api/opinions/awesome/${this.review.id}/`, config)
                    .then(res => res.json())
                    .then((data) => {
                        console.log('data', data)
                        this.$store.dispatch('opinion/toggleAwesomeOpinion', {opinionId:data.id, reviewId:this.review.id})
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

                fetch(`${this.$baseUrl}/api/opinions/random/${this.review.id}/`, config)
                    .then(res => res.json())
                    .then((data) => {
                        console.log('data', data)
                        this.$store.dispatch('opinion/toggleRandomOpinion', {opinionId:data.id, reviewId:this.review.id})
                    })
            },
        },


    }
</script>

<style lang="scss">
    @import "~bulma";

    .container {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        width: 80%;
        text-align: left;
    }

    .user_pic {
        height: 100% !important;
        width: auto !important;
    }
</style>


