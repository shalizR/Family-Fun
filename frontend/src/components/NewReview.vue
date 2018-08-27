<template>
    <div>
        <h1>New review</h1>
        <div id="container">
            <div class="field">
                <lable class="label">Rating</lable>
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
            <div class="field">
                <lable class="label">Rating</lable>
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
            <div class="field">
                <label class="label">Content</label>
                <div class="control">
                    <textarea class="textarea" placeholder="Textarea" v-model="params.content"></textarea>
                </div>
            </div>

            <div class="control">
                <button class="button is-link">Submit</button>
            </div>

        </div>
    </div>
    
</template>

<script>
export default {
        name: "NewReview",
        data () {
            return {
                params: {
                    content: '',
                    rating: Number,
                    priceLevel: Number,
                    highChair: Boolean,
                    steps: Boolean,
                    changingTable: Boolean,
                    placeForStroller: Boolean,
                    isNoisy: Boolean,
                    friendlyWaitingStaff: Boolean,
                    tablecloth: Boolean,
                    quickService: Boolean,
                }
            }
        },
        methods: {
            // ...mapActions('restaurantDetail', [
            //     'submitNewReview'
            // ]),
           // submitNewReview() {
           //
           // }
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

    }

</style>
