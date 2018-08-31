<template>
    <div class="new-review-container">
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
                    <select v-model="params.changingTable">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is it noisy?</span>
                <div class="select select-container">
                    <select v-model="params.isNoisy">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is there high chairs for children?</span>
                <div class="select select-container">
                    <select v-model="params.highChair">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Are the waiting staff sympathetic?</span>
                <div class="select select-container">
                    <select v-model="params.staff">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="new-review-dropdowns">
            <div class="select-label">
                <span class="label">Price level</span>
                <div class="select select-container">
                    <select v-model="params.priceLevel">
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
                    <select v-model="params.stroller">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Are there steps?</span>
                <div class="select select-container">
                    <select v-model="params.steps">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Is the service quick?</span>
                <div class="select select-container">
                    <select v-model="params.quickService">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
            <div class="select-label">
                <span class="label">Are tables covered with tablecloths?</span>
                <div class="select select-container">
                    <select v-model="params.tablecloth">
                        <option value="Yes">Yes</option>
                        <option value="No">No</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="new-review-submit">
            <lu-button class="new-review-button" @click="handleSubmit">Submit</lu-button>
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
