<template>
    <div>
        <button type="button" class="btn btn-primary" v-on:click="test">TEST</button>
        <button type="button" class="btn btn-primary" v-on:click="test_get">GET</button>
        <button type="button" class="btn btn-primary" v-on:click="test_post">POST</button>
        <button type="button" class="btn btn-primary" v-on:click="test_put">PUT</button>
        <button type="button" class="btn btn-primary" v-on:click="test_delete">DELETE</button>
    </div>
    <div>
        <form v-on:click="search">
            <div>
                <label for="name">name:</label>
                <input id="name" type="text" v-model="name">
            </div>
            <button type="button">search</button>
            <p>{{ name }}</p>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            name: '',
        }
    },
    methods: {
        search: function() {
            console.log(this.name)
            axios('http://127.0.0.1:5000/search', {
                method: "get",
                params: {
                    name: this.name,
                },
            })
            .then(function(response){
                console.log(response);
            })
            .catch(function(error){
                console.log(error);
            });
        },
        test_get: () => {
            axios('http://127.0.0.1:5000/test', {
                method: "get",
                params: {
                    name: "test_get",
                },
            })
            .then((response) => {
                console.log(response.data["status"]);
            })
            .catch((error) => {
                console.log(error);
            });
        },
        test_post: () => {
            axios('http://127.0.0.1:5000/test', {
                method: "post",
                data: {
                    value: "test_post",
                },
            })
            .then((response) => {
                console.log(response.data["status"]);
            })
            .catch((error) => {
                console.log(error);
            });
        },
        test_put: () => {
            axios('http://127.0.0.1:5000/test', {
                method: "put",
                params: {
                    value: "test_put",
                },
            })
            .then((response) => {
                console.log(response.data["status"]);
            })
            .catch((error) => {
                console.log(error);
            });
        },
        test_delete: () => {
            axios('http://127.0.0.1:5000/test', {
                method: "delete",
                params: {
                    value: "test_delete",
                },
            })
            .then((response) => {
                console.log(response.data["status"]);
            })
            .catch((error) => {
                console.log(error);
            });
        },
    }
};
</script>