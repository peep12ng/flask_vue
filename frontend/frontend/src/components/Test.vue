<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Test',
    data() {
        return {
            msg: 'aa',
        };
    },
    methods: {
        getMessage() {
            const path = 'http://127.0.0.1:5000/main';
            axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error) => {

                    console.error(error);
                });
        },
    },
    created() {
        this.getMessage();
    },
};
</script>