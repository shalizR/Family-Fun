<template>
    <div class="container">
        <div class="columns">
            <div class="column is-8 is-offset-2">
        <div>
            <h1 class="title new-review-title">Add A Review</h1>
            <div class="field">
                <span class="label">Content</span>
                <div class="control">
                    <textarea class="textarea" placeholder="Textarea" v-model="params.content"></textarea>
                </div>
            </div>
        </div>
        <div class="new-review-dropdowns">
            <div class="select-label">
                <span class="label">Rating</span>
                <div class="select select select-container">
                    <select v-model="params.rating">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
            </div>

            <div class="select-label">
                <span class="label">Is there a changing table?</span>
                <div class="select select-container">
                    <select v-model="params.has_changing_table">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is it noisy?</span>
                <div class="select select-container">
                    <select v-model="params.isNoisy">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is there high chairs for children?</span>
                <div class="select select-container">
                    <select v-model="params.high_chair">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Are the waiting staff sympathetic?</span>
                <div class="select select-container">
                    <select v-model="params.friendly_waiting_staff">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="new-review-dropdowns">
            <div class="select-label">
                <span class="label">Price level</span>
                <div class="select select-container">
                    <select v-model="params.price_level">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is there place for strollers?</span>
                <div class="select select-container">
                    <select v-model="params.place_for_stroller">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Are there steps?</span>
                <div class="select select-container">
                    <select v-model="params.are_there_steps">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is the service quick?</span>
                <div class="select select-container">
                    <select v-model="params.has_quick_service">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Are tables covered with tablecloths?</span>
                <div class="select select-container">
                    <select v-model="params.has_tablecloth">
                        <option :value="true">Yes</option>
                        <option :value="false">No</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="new-review-submit">
            <lu-button class="new-review-button" @click="handleSubmit">Submit</lu-button>
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
        data () {
            return {
                params: {
                    content: '',
                    rating: null,
                    priceLevel: null,
                    highChair: null,
                    steps: null,
                    changingTable: null,
                    stroller: null,
                    isNoisy: null,
                    staff: null,
                    tablecloth: null,
                    quickService: null,
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
            handleSubmit () {
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

    .new-review-title {
        font-size: 2em;
    }

    .new-review-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 70%;
        font-family: 'Varela Round', sans-serif;
        margin: 0 auto;
    }

    .new-review-dropdowns {
        display: flex;
        align-self: center;
    }

    .select-container {
        display: flex;
        flex-direction: column;
        height: 100px;
    }

    .select-label {
        margin: 20px 10px;
        width: 30%;
        height: 100px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .new-review-submit {
        margin: 10px auto;
    }

    .new-review-button {
        color: white;
        background: orange;
    }
</style>
