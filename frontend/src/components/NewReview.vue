<template>
    <div class="container">
        <div class="columns">
            <div class="column is-6">
                <h1 class="title is-4">Add a review</h1>
            </div>
        </div>
        <div class="columns">
            <div class="column is-8">
                <div class="field">
                    <span class="label">Content</span>
                    <div class="control">
                        <textarea class="textarea" placeholder="Textarea" v-model="params.content"></textarea>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3">
                <span class="label">Rating</span>
                <div class="select">
                    <select v-model="params.rating">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
                <span class="label">Is there a baby changing table?</span>
                <div class="select">
                    <select v-model="params.changingTable">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
                <span class="label">Is there noisy?</span>
                <div class="select">
                    <select v-model="params.isNoisy">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
                <span class="label">Is there high chairs for children?</span>
                <div class="select">
                    <select v-model="params.highChair">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
                <span class="label">Are the waiting staff sympathetic?</span>
                    <div class="select">
                        <select v-model="params.staff">
                            <option value="Yes">Yes</option>
                            <option value="No">No</option>
                        </select>
                    </div>
            </div>
            <div class="column is-3">
                <span class="label">Price level</span>
                    <div class="select">
                        <select v-model="params.priceLevel">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                        </select>
                    </div>
                <span class="label">Is there a place for stroller?</span>
                <div class="select">
                    <select v-model="params.stroller">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
                <span class="label">Are there steps?</span>
                <div class="select">
                    <select v-model="params.steps">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
                <span class="label">Is the service quick?</span>
                <div class="select">
                    <select v-model="params.quickService">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
                <span class="label">Are tables covered with tablecloths?</span>
                    <div class="select">
                        <select v-model="params.tablecloth">
                            <option value="Yes">Yes</option>
                            <option value="No">No</option>
                        </select>
                    </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-6">
                    <lu-button @click="handleSubmit">Submit</lu-button>
                </div>
            </div>
        </div>
</template>

<script>
    import {mapActions, mapState} from 'vuex';
    import Button from './Button';

    export default {
        name: "NewReview",
        data() {
            return {
                params: {
                    content: '',
                    rating: null,
                    priceLevel: null,
                    highChair: false,
                    steps: false,
                    changingTable: false,
                    stroller: false,
                    isNoisy: false,
                    staff: false,
                    tablecloth: false,
                    quickService: false,
                }
            }
        },
        props: ['id'],
        components: {
            Button
        },
        computed: {
            ...mapState('restaurantDetail', {
                newReview: (state) => state.newReview,

            })
        },
        methods: {
            ...mapActions('restaurantDetail', [
                'submitNewReview',

            ]),
            handleSubmit() {

                this.$store.dispatch('restaurantDetail/submitNewReview', {params: this.params, id: this.id})
                    .then(() => {
                        this.$router.push({name: 'RestaurantDetail'})
                    })
            },


            setSelectedSearch: function () {
                this.fetchRestaurants({search_text: this.search_text, category: this.category});
            },


        }
    }
</script>

<style lang="scss" scoped>
    @import "~bulma";


    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%;
        font-family: 'Varela Round', sans-serif;
        text-align: left;
    }
</style>
