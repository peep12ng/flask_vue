<template>
    <div>
        {{ this.test }}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return{
            test: '',
        }
    },
    created(){
        axios('http://127.0.0.1:5000/search', {
            method: "get",
            params: {
                name: this.$route.params.id,
            },
        })
        .then(function(response){
            console.log(response.data.puuid);
            this.test = response.data['puuid'];
        })
        .catch(function(error){
            console.log(error);
        });        
    }
}
</script>

<style>

</style>