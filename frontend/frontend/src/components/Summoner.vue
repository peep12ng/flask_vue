<template>
    <div>
        {{ test }}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            test: 'aa',
        }
    },
    created(){
        axios('http://127.0.0.1:5000/search', {
            method: "get",
            params: {
                name: this.$route.params.id,
            },
        })
        .then(response => {
            console.log(response);
            this.test = response.data['puuid'];
        })
        .catch(error => {
            console.log(error);
        });        
    }
}
</script>

<style>

</style>