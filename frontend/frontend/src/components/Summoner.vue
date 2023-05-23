<template>
    <div>
        {{ this.$route.params.id }}
    </div>
</template>

<script>
// import axios from 'axios';

export default {
    data(){
        return{
            test: '',
        }
    },
    created(){
        // axios('http://127.0.0.1:5000/search', {
        //     method: "get",
        //     params: {
        //         name: this.$route.params.id,
        //     },
        // })
        // .then(function(response){
        //     this.test = response;
        // })
        // .catch(function(error){
        //     console.log(error);
        // });        
    }
}
</script>

<style>

</style>