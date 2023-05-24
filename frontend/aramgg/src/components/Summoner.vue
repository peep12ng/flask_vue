<template>
  <div id="summoner">
    <div class="summoner-match">
        <ul>
            <li v-for="matchList in summonerMatch" :key="matchList" class="matchList">
                <div class="matchList-wrap">
                    <div class="match-info">
                        <b v-if="matchList.isWin == true" class="resultWin">승리</b>
                        <b v-if="matchList.isWin == false" class="resultLose">패배</b>
                        <p>15분 57초</p>
                        <p>3일전</p>
                    </div>
                    <div class="summoner-champ">
                        <div class="champ">
                            <img src="http://ddragon.leagueoflegends.com/cdn/13.8.1/img/champion/Fiddlesticks.png" alt="">
                            <i>18</i>
                        </div>
                        <div class="spells">
                            <div class="spell1">
                                <img src="http://ddragon.leagueoflegends.com/cdn/13.8.1/img/spell/SummonerFlash.png" alt="">
                            </div>
                            <div class="spell2">
                                <img src="http://ddragon.leagueoflegends.com/cdn/13.8.1/img/spell/SummonerFlash.png" alt="">
                            </div>
                        </div>
                        <div class="runes">
                            <div class="primaryRune">
                                <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                            </div>
                            <div class="subRune">
                                <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                            </div>
                        </div>
                    </div>                    
                    <div class="summoner-kda">
                        <p class="kda-top">{{ matchList.kills }}/{{ matchList.deaths }}/{{ matchList.assists }}</p>
                        <p v-if="Math.round((matchList.kills+matchList.assists)/matchList.deaths*100)/100 != Infinity" class="kda-bottom">{{ Math.round((matchList.kills+matchList.assists)/matchList.deaths*100)/100 }} KDA</p>
                        <p v-if="Math.round((matchList.kills+matchList.assists)/matchList.deaths*100)/100 == Infinity" class="kda-bottom">Perfect KDA</p>                        
                    </div>
                </div>
            </li>
        </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return{
            summonerMatch: [],
        }
    },
    created(){
        axios('http://127.0.0.1:5000/search', {
            method: "get",
            params: {
                name: this.$route.params.id,
            },
        })
        .then( response =>{
            this.summonerMatch = response.data;
            console.log(response);
        })
        .catch( error => {
            console.log(error);
        } );      
    }
}
</script>

<style>
@import "../assets/css/reset.css";

#summoner {
    width: 100%; max-width: 1140px;
    margin: 0 auto; 
}

.summoner-match {

}

.matchList {
    width: 100%;
    margin-bottom: 10px;
    border-top: 1px solid #e6e6e6;
    border-bottom: 1px solid #e6e6e6;
    box-sizing: border-box;
}

.matchList-wrap {
    display: flex;
    height: 98px;
    align-items: center;
    background: #fef9f9;
}

.matchList-wrap-win {
    background: #f9fbfd;
}

.match-info {
    width: 112px;
    text-align: center;
}

.match-info b {
    font-size: 14px;
}

.match-info p {
    font-size: 12px;
    margin-bottom: 2px;
}

.match-info p:last-child {
    margin-bottom: 0px;
}

.resultWin {
    color: #207ac7;
}

.resultLose {
    color: #ed6767;
}

.summoner-champ {
    display: flex;
}

.champ {
    position: relative;
    width: 52px;
    height: 52px;
    margin-right: 4px;
}

.champ img {
    width: 100%;
}

.champ i {
    position: absolute;
    bottom: 0; right: 0;
    display: block;
    width: 20px;
    height: 20px;
    background: rgba(0,0,0, 0.4);
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    text-align: center;
}

.spells {
    margin-right: 4px;
}

.spells>div {
    width: 24px;
    height: 24px;
}

.spell1 {
    margin-bottom: 4px;
}

.spells>div img {
    width: 100%;
    height: 100%;
}

.runes {

}

.primaryRune {
    margin-bottom: 4px;
}

.runes>div {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #000;
    text-align: center;
}

.primaryRune img {
    width: 20px;
    height: 20px;
    padding: 2px 0;
}

.subRune img {
    width: 16px;
    height: 16px;
    padding: 4px 0;
}

.summoner-kda {
    width: 160px;
    text-align: center;
}

.kda-top {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 3px;
}

.kda-bottom {
    font-size: 12px;
}

</style>