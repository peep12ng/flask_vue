<template>
    <div id="search">
      <div class="search-wrap">
        <input class="search" placeholder="검색" type="text" @keyup.enter="search()">
        <div class="search-btn-wrap">
          <a href="javascript:" class="search-btn" @click="search()">
            <i class="material-symbols-outlined">search</i>
          </a>
        </div>
      </div>
    </div>  
</template>

<script>
import $ from 'jquery';

export default {
    data(){
        return{

        }
    },
    methods: {
        search(){
          var inputValue = $('.search').val();

          if(inputValue==''){
              alert('검색어를 입력하세요');
          }
          else{
            this.$router.push(`/summoner/${ inputValue }`);
          }
        },        
    }
}
</script>

<style>

</style>