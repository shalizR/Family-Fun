<template>
    <div id="container">
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <h1 class="title is-4">Add a review</h1>
            </div>
        </div>
        <div class="columns">
            <div class="column is-8 is-offset-3">
                <div class="field">
                    <span class="label">Content</span>
                    <div class="control">
                        <textarea class="textarea" placeholder="Textarea" v-model="params.content"></textarea>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Rating</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.rating">
                                <option v-bind:value="1">1</option>
                                <option v-bind:value="2">2</option>
                                <option v-bind:value="3">3</option>
                                <option v-bind:value="4">4</option>
                                <option v-bind:value="5">5</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Price level</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.priceLevel">
                                <option v-bind:value="1">1</option>
                                <option v-bind:value="2">2</option>
                                <option v-bind:value="3">3</option>
                                <option v-bind:value="4">4</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Is there a baby changing table?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.changingTable">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Is there a place for stroller?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.stroller">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Is there noisy?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.isNoisy">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Are the waiting staff sympathetic?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.staff">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Is there high chairs for children?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.highChair">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Are there steps?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.steps">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Is the service quick?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.quickService">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="column is-3 is-offset-3">
                <div class="field">
                    <span class="label">Are tables covered with tablecloths?</span>
                    <div class="control">
                        <div class="select">
                            <select v-model="params.tablecloth">
                                <option v-bind:value="None">None</option>
                                <option v-bind:value="Yes">Yes</option>
                                <option v-bind:value="No">No</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column is-6 is-offset-3">
                <div class="control">
                    <lu-button class="button is-link" @click="handleSubmit">Submit</lu-button>
                </div>
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
        created() {
            console.log('created', this.id)
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

<style lang="scss">
    @import "~bulma";


    #container {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        width: 100%;
        font-family: 'Varela Round', sans-serif;
        text-align: left;

    }
    .field {
        text-align: left;
    }


</style>
