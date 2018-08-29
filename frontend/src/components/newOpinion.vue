<template>
    <div class="content">
        <div v-for="opinion in opinions" :key="opinion.id" id="opinion">
            <h6>{{opinion.user.username}}</h6>
            <h6 v-if="helpful">{{opinion}}</h6>
        </div>
    </div>
    <h3 v-if="place_for_stroller">Place for stroller? Yes</h3>
    <h3 v-else-if="!place_for_stroller">Place for stroller? No</h3>
    
</template>

<script>
    import {mapActions, mapState} from 'vuex';
    import Button from './Button';

    export default {
        name: "NewOpinion",
        data() {
            return {
                params: {
                    helpful: false,
                    awesome: false,
                    random: false,
                }
            }
        },
        props: ['id'],
        components: {
            Button
        },
        computed: {
            ...mapState('reviewCard', {
                newOpinion: (state) => state.newOpinion,

            })
        },
        created() {
            console.log('created', this.id)
        },
        methods: {
            ...mapActions('reviewCard', [
                'handleHelpfulOpinion',
                'handleAwesomeOpinion',
                'handleRandomOpinion',

            ]),
        },
    }

</script>

<style scoped>

</style>