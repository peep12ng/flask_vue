<template>
  <div id="summoner">
    <div class="summoner-match">
        <ul>
            <li v-for="matchList in summonerMatch" :key="matchList" class="matchList">
                <div class="matchList-wrap-container">
                    <div class="matchList-wrap" :style="`border-left: 8px solid ${ matchList.isWin ? '#5393ca' : '#ed6767' }; background: ${ matchList.isWin ? '#f9fbfd' : '#fef9f9' }`">
                        <div class="match-data">
                            <div class="match-info">
                                <b v-if="matchList.isWin" class="resultWin">승리</b>
                                <b v-else class="resultLose">패배</b>
                                <p>{{ matchList.timeplayedMinutes }}분 {{ matchList.timeplayedSeconds }}초</p>
                                <p>{{ matchList.date }}</p>
                            </div>
                            <div class="summoner-champ">
                                <div class="champ">
                                    <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                    <i>{{ matchList.champLevel }}</i>
                                </div>
                                <div class="spells">
                                    <div class="spell1">
                                        <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                    </div>
                                    <div class="spell2">
                                        <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
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
                            <div class="summoner-killGold">
                                <p class="killPercent">킬 관여 <b>100</b>%</p>
                                <p class="goldEarned"><img src="../assets/image/coins.png" alt=""> <b>{{ matchList.goldEarned.toLocaleString('ko-KR') }}</b></p>
                            </div>   
                            <div class="summoner-items">
                                <ul>
                                    <li class="itemList" v-for="items in matchList.items" :key="items">
                                        <div>
                                            <img v-if="items.slice(-4) != Number('0000')" :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/${ items.slice(-4) }.png`" alt="">
                                        </div>
                                    </li>
                                </ul>
                            </div> 
                        </div>
                        <div class="match-participants">
                            <div class="match-participants-wrap">
                                <ul class="participants-list-container">
                                    <li v-for="blue in 5" :key="blue" class="participants-list">
                                        <div class="participants-list-wrap">
                                            <span class="participants-champ">
                                                <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                            </span>
                                            <p class="participants-name">때리는걸잘해요</p>
                                        </div>
                                    </li>
                                </ul>
                                <ul class="participants-list-container">
                                    <li v-for="red in 5" :key="red" class="participants-list">
                                        <div class="participants-list-wrap">
                                            <span class="participants-champ">
                                                <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                            </span>
                                            <p class="participants-name">때리는걸잘해요</p>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="match-detail-open" :style="`background: ${ matchList.isWin ? '#5393ca' : '#ed6767' }`">
                        <a href="javascript:" @click="matchList.openDetail = !matchList.openDetail">
                            <i v-if="matchList.openDetail" class="material-symbols-outlined">expand_less</i>
                            <i v-else class="material-symbols-outlined">expand_more</i>
                        </a>
                    </div>
                </div>
                <div v-if="matchList.openDetail" class="match-detail">
                    <div class="matchList-detail-tab">
                        <ul>
                            <li v-for="(matchDetail,i) in matchDetailTAb" :key="matchDetail">
                                <div>
                                    <a href="javascript:" class="detailTabBtn" :class="{ detailTabClicked: matchList.detailTabOpen[i] }" @click="matchList.detailTabOpen[0] = false, matchList.detailTabOpen[1] = false, matchList.detailTabOpen[2] = false, matchList.detailTabOpen[i] = true">{{ matchDetail }}</a>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div v-if="matchList.detailTabOpen[0]" class="matchList-detail-table">
                        <div class="detail-table-container">
                            <div class="detail-table-team">
                                <div class="detail-th" :style="`border-top: 1px solid #5393ca; background: #dde9f3`">
                                    <div class="detail-th-wrap">
                                        <p class="detail-th-result" :style="`color: #207ac7`">승리</p>
                                    </div>
                                    <div class="detail-th-wrap">
                                        <p class="detail-th-kda">KDA</p>
                                        <p class="detail-th-damage">
                                            <i class="material-symbols-outlined" @click="matchList.blueDamage = !matchList.blueDamage">arrow_left</i>
                                            <span v-if="matchList.blueDamage">가한 피해량</span>
                                            <span v-else>받은 피해량</span>
                                            <i class="material-symbols-outlined" @click="matchList.blueDamage = !matchList.blueDamage">arrow_right</i>
                                        </p>
                                        <span class="detail-th-kills">
                                            <i class="material-symbols-outlined">swords</i>
                                            <span :style="`color: #207ac7`">50</span>
                                        </span>
                                    </div>
                                </div>
                                <div class="detail-tbody">
                                    <ul class="detail-tbody-wrap">
                                        <li v-for="detailBlueList in matchList.blue" :key="detailBlueList" class="detail-tbody-list" :style="`background: #f9fbfd`">
                                            <div class="detail-tbody-list-wrap">
                                                <div class="detail-content detail-champInfo">
                                                    <div class="detail-champ">
                                                        <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                                        <i>{{ detailBlueList.champLevel }}</i>                                                        
                                                    </div>
                                                    <div class="detail-spells">
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="detail-runes">
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-name">
                                                    <p>때리는걸잘해요</p>
                                                </div>
                                                <div class="detail-content detail-kda">
                                                    <p class="detail-kda-top">{{ detailBlueList.kills }}/{{ detailBlueList.deaths }}/{{ detailBlueList.assists }}</p>
                                                    <p v-if="Math.round((detailBlueList.kills+detailBlueList.assists)/detailBlueList.deaths*100)/100 != Infinity" class="detail-kda-bottom">{{ Math.round((detailBlueList.kills+detailBlueList.assists)/detailBlueList.deaths*100)/100 }} KDA</p>
                                                    <p v-if="Math.round((detailBlueList.kills+detailBlueList.assists)/detailBlueList.deaths*100)/100 == Infinity" class="detail-kda-bottom">Perfect KDA</p>                        
                                                    
                                                </div>
                                                <div class="detail-content detail-damage">
                                                    <div class="detail-damage-graph" v-if="matchList.blueDamage">
                                                        <p>15,770</p>
                                                        <i :style="`width: 50%`"></i>
                                                    </div>
                                                    <div class="detail-damage-graph" v-else>
                                                        <p>15,770</p>
                                                        <i :style="`width: 70%`"></i>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-items">
                                                    <ul class="detail-items-wrap">
                                                        <li class="detail-item-list" v-for="blueItems in detailBlueList.items" :key="blueItems">
                                                            <div class="detail-item-list-wrap">
                                                                <img v-if="blueItems.slice(-4) != Number('0000')" :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/${ blueItems.slice(-4) }.png`" alt="">
                                                            </div>
                                                        </li>
                                                    </ul>                                                    
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>                           
                            </div>
                            <div class="detail-table-team">
                                <div class="detail-th" :style="`border-top: 1px solid #ed6767; background: #f6e5e5`">
                                    <div class="detail-th-wrap">
                                        <span class="detail-th-kills">
                                            <i class="material-symbols-outlined">swords</i>
                                            <span :style="`color: #ed6767`">50</span>
                                        </span> 
                                        <p class="detail-th-kda">KDA</p>                                        
                                        <p class="detail-th-damage">
                                            <i class="material-symbols-outlined" @click="matchList.redDamage = !matchList.redDamage">arrow_left</i>
                                            <span v-if="matchList.redDamage">가한 피해량</span>
                                            <span v-else>받은 피해량</span>
                                            <i class="material-symbols-outlined" @click="matchList.redDamage = !matchList.redDamage">arrow_right</i>
                                        </p>                                                                               

                                    </div>
                                    <div class="detail-th-wrap">
                                        <span class="detail-th-result" :style="`color: #ed6767`">패배</span>
                                    </div>                                    
                                </div> 
                                <div class="detail-tbody">
                                    <ul class="detail-tbody-wrap">
                                        <li v-for="detailRedList in matchList.red" :key="detailRedList" class="detail-tbody-list" :style="`background: #fef9f9`">
                                            <div class="detail-tbody-list-wrap">
                                                <div class="detail-content detail-champInfo">
                                                    <div class="detail-champ">
                                                        <img :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Aatrox.png`" alt="">
                                                        <i>{{ detailRedList.champLevel }}</i>                                                        
                                                    </div>
                                                    <div class="detail-spells">
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                        <div class="detail-spell">
                                                            <img src="http://ddragon.leagueoflegends.com/cdn/13.10.1/img/spell/SummonerFlash.png" alt="">
                                                        </div>
                                                    </div>
                                                    <div class="detail-runes">
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                        <div class="detail-rune">
                                                            <img src="https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png" alt="">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-name">
                                                    <p>때리는걸잘해요</p>
                                                </div>
                                                <div class="detail-content detail-kda">
                                                    <p class="detail-kda-top">{{ detailRedList.kills }}/{{ detailRedList.deaths }}/{{ detailRedList.assists }}</p>
                                                    <p v-if="Math.round((detailRedList.kills+detailRedList.assists)/detailRedList.deaths*100)/100 != Infinity" class="detail-kda-bottom">{{ Math.round((detailRedList.kills+detailRedList.assists)/detailRedList.deaths*100)/100 }} KDA</p>
                                                    <p v-if="Math.round((detailRedList.kills+detailRedList.assists)/detailRedList.deaths*100)/100 == Infinity" class="detail-kda-bottom">Perfect KDA</p>                        
                                                    
                                                </div>
                                                <div class="detail-content detail-damage">
                                                    <div class="detail-damage-graph" v-if="matchList.redDamage">
                                                        <p>15,770</p>
                                                        <i :style="`width: 50%`"></i>
                                                    </div>
                                                    <div class="detail-damage-graph" v-else>
                                                        <p>15,770</p>
                                                        <i :style="`width: 70%`"></i>
                                                    </div>
                                                </div>
                                                <div class="detail-content detail-items">
                                                    <ul class="detail-items-wrap">
                                                        <li class="detail-item-list" v-for="redItems in detailRedList.items" :key="redItems">
                                                            <div class="detail-item-list-wrap">
                                                                <img v-if="redItems.slice(-4) != Number('0000')" :src="`http://ddragon.leagueoflegends.com/cdn/13.10.1/img/item/${ redItems.slice(-4) }.png`" alt="">
                                                            </div>
                                                        </li>
                                                    </ul>                                                    
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>                                 
                            </div>
                        </div>
                    </div>
                    <div v-if="matchList.detailTabOpen[1]" class="matchList-detail-build">
                        build
                    </div>
                    <div v-if="matchList.detailTabOpen[2]" class="matchList-detail-teamAnalyze">
                        teamAnalyze
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
            matchDetailTAb: ['종합','빌드','팀 분석'],
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
            console.log(response);
            for( var i=0; i<response.data.length; i++ ){
                 this.summonerMatch[i] = {
                    items: [],
                    detailTabOpen: [true,false,false],
                    openDetail: false,
                    blueDamage: true,
                    redDamage: true,
                    blue: [{},{},{},{},{}],               
                    red: [{},{},{},{},{}],               
                }
                
                // items
                this.summonerMatch[i].items.push(response.data[i].myData.item0_id);
                this.summonerMatch[i].items.push(response.data[i].myData.item1_id);
                this.summonerMatch[i].items.push(response.data[i].myData.item2_id);
                this.summonerMatch[i].items.push(response.data[i].myData.item6_id);
                this.summonerMatch[i].items.push(response.data[i].myData.item3_id);
                this.summonerMatch[i].items.push(response.data[i].myData.item4_id);
                this.summonerMatch[i].items.push(response.data[i].myData.item5_id);

                // kda
                this.summonerMatch[i].kills = response.data[i].myData.kills;
                this.summonerMatch[i].assists = response.data[i].myData.assists;
                this.summonerMatch[i].deaths = response.data[i].myData.deaths;
                
                // gold
                this.summonerMatch[i].goldEarned = response.data[i].myData.goldEarend;

                // isWin
                this.summonerMatch[i].isWin = response.data[i].myData.isWin;
                
                // champLevel
                this.summonerMatch[i].champLevel = response.data[i].myData.champLevel;

                // time
                var gameStartTime = response.data[i].gameStartTimeStamp;
                var now = new Date();
                var dataDiff = Math.abs((gameStartTime-now)/(1000*60*60));

                if(dataDiff<24){
                    this.summonerMatch[i].date = `${Math.floor(dataDiff)}시간 전`;
                }
                else{
                    this.summonerMatch[i].date = `${Math.floor(dataDiff/24)}일 전`;
                }                

                // playTime
                var hours = Math.floor(response.data[i].gameDuration/3600);
                var minutes = Math.floor( (response.data[i].gameDuration - hours*3600)/60 );
                var seconds = response.data[i].gameDuration - hours*3600 - minutes*60;

                this.summonerMatch[i].timeplayedMinutes = minutes;
                this.summonerMatch[i].timeplayedSeconds = seconds;    
                
                
                // blue/red
                for( var k=0; k<5; k++ ){
                    this.summonerMatch[i].blue[k].items = [];
                    this.summonerMatch[i].red[k].items = [];

                    // blue kda
                    this.summonerMatch[i].blue[k].kills = response.data[i].participants[k].kills;
                    this.summonerMatch[i].blue[k].deaths = response.data[i].participants[k].deaths;
                    this.summonerMatch[i].blue[k].assists = response.data[i].participants[k].assists;

                    // red kda
                    this.summonerMatch[i].red[k].kills = response.data[i].participants[k+5].kills;
                    this.summonerMatch[i].red[k].deaths = response.data[i].participants[k+5].deaths;
                    this.summonerMatch[i].red[k].assists = response.data[i].participants[k+5].assists;

                    // blue champLevel
                    this.summonerMatch[i].blue[k].champLevel = response.data[i].participants[k].champLevel;

                    // red champLevel
                    this.summonerMatch[i].red[k].champLevel = response.data[i].participants[k+5].champLevel;

                    // blue items
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item0_id);
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item1_id);
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item2_id);
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item3_id);
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item4_id);
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item5_id);
                    this.summonerMatch[i].blue[k].items.push(response.data[i].participants[k].item6_id);

                    // red items
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item0_id);
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item1_id);
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item2_id);
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item3_id);
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item4_id);
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item5_id);
                    this.summonerMatch[i].red[k].items.push(response.data[i].participants[k+5].item6_id);



                }

                
            }
            console.log(this.summonerMatch);
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

.matchList-wrap-container {
    position: relative;
    width: 100%;
    height: 100px;
}

.matchList-wrap {
    display: flex;
    justify-content: space-between;
    height: 100%;
}

.match-data {
    display: flex;
    height: 100%;
    align-items: center;
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

.summoner-killGold {
    width: 120px;
}

.killPercent {
    font-size: 12px;
}

.goldEarned {
    font-size: 12px;
}

.goldEarned img {
    width: 18px;
}

.summoner-items {

}

.summoner-items ul {
    width: 124px;
    display: flex;
    flex-wrap: wrap;
}

.itemList {
    width: 28px;
    height: 28px;
    margin-right: 2px;
    margin-bottom: 2px;
}

.itemList div {
    width: 100%;
    height: 100%;
    background: #e6e6e6;
}

.itemList img {
    width: 100%;
}

.match-participants {
    display: flex;
    padding-right: 30px;
}

.match-participants-wrap {
    display: flex;
    align-items: center;
}

.participants-list-container {
    
}

.participants-list {
    width: 144px;
}

.participants-list-wrap {
    display: flex;
}

.participants-champ {
    display: block;
    width: 14px;
    height: 14px;
    margin-right: 2px;
    margin-bottom: 2px;
}

.participants-champ img {
    width: 100%;
}

.participants-name {
    font-size: 11px;
    line-height: 14px;
    color: #808080;
}

.match-detail-open {
    position: absolute;
    top: 0; right: 0;
    display: block;
    width: 30px;
    height: 100%;
}

.match-detail-open a {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    text-align: center;
    width: 100%;
    height: 100%;
}

.match-detail-open i {
    display: flex;
    color: #fff;
}

.match-detail {
    width: 100%;
    border: 1px solid #e6e6e6;
    border-bottom: 0;
    box-sizing: border-box;
}

.matchList-detail-tab {
    width: 100%;
    background: #fafafa;
}

.matchList-detail-tab ul {
    padding: 9px 16px;
    display: flex;
}

.matchList-detail-tab li {
    display: flex;
}

.detailTabBtn {
    display: block;
    padding: 10px 16px;
    font-size: 12px;
    color: #808080;
}

.detailTabClicked {
    color: #fff;
    background: #363944;
    border-radius: 16px;
}

.matchList-detail-table {
    width: 100%;
}

.detail-table-container {
    display: flex;
    width: 100%;

}

.detail-table-team {
    display: flex;
    flex-grow: 1;
    flex-direction: column;
}

.detail-table-team:first-child {
    border-right: 1px solid #e6e6e6;
}


.detail-th {
    display: flex;
    padding: 0 12px;
    height: 40px;
    justify-content: space-between;
    align-items: center;
}

.detail-th-wrap {
    display: flex;    
}

.detail-th-wrap p {
    display: flex;
    font-size: 12px;
}

.detail-th-result {
    font-weight: bold;
    font-size: 12px;
}

.detail-th-kda {
    width: 62px;
    justify-content: center;
    align-items: center;
}

.detail-th-damage {
    width: 143px;
    justify-content: center;
    align-items: center;
}

.detail-th-damage i {
    cursor: pointer;
}

.detail-th-kills {
    display: flex;
    width: 152px;
    justify-content: flex-end;
    align-items: center;
}

.detail-th-kills i {
    font-size: 16px;
}

.detail-th-kills span {
    font-size: 12px;
}

.detail-table-team:last-child .detail-th-kills {
    display: flex;
    width: 187px;
    justify-content: flex-start;
    align-items: center;
}

.detail-tbody {
    display: flex;
}

.detail-tbody-wrap {

}

.detail-tbody-list {
    border-bottom: 1px solid #e6e6e6;
    box-sizing: border-box;
}

.detail-tbody-list:last-child {
    border-bottom: 0;
}

.detail-tbody-list-wrap {
    display: flex;
    padding: 12px;
}

.detail-content {
    display: flex;
}

.detail-champInfo {
    width: 70px;
    justify-content: space-between;
}

.detail-champ {
    display: flex;
    position: relative;
    width: 34px;
    height: 34px;
}

.detail-champ img {
    width: 100%;
}

.detail-champ i {
    position: absolute;
    bottom: 0; right: 0;
    display: block;
    width: 18px;
    height: 18px;
    background: rgba(0,0,0, 0.4);
    color: #fff;
    font-size: 11px;
    font-weight: bold;
    text-align: center;
}

.detail-spells {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.detail-spell {
    display: flex;
    width: 16px;
}

.detail-spell img {
    width: 100%;
}


.detail-runes {
    display: flex;
    flex-direction: column;
    justify-content: space-between;    
}

.detail-rune {
    display: flex;
    justify-content: center;
    align-items: center;    
    width: 16px;
    height: 16px;
    background: #000;
    border-radius: 50%;
}

.detail-rune img {
    display: flex;
    width: 12px;

}


.detail-name {
    width: 113px;
    padding-left: 4px;
    align-items: center;
}

.detail-name p {
    display: flex;
    font-size: 11px;
    color: #000;
}

.detail-kda {
    width: 62px;
    flex-direction: column;
    align-items: center;
}

.detail-kda p {
    display: flex;
}

.detail-kda-top {
    font-size: 12px;
    font-weight: bold;
}

.detail-kda-bottom {
    font-size: 11px;
    margin-top: 2px;
}

.detail-damage {
    width: 143px;
    align-items: center;
}

.detail-damage-graph {
    display: flex;
    position: relative;
    width: 100px;
    height: 14px;
    background: #808080;
    margin: 0 auto;
}

.detail-damage-graph p {
    position: relative;
    display: block;
    width: 100%;
    z-index: 2;
    font-size: 12px;
    color: #fff;
    font-weight: bold;
    text-align: center;
    line-height: 14px;
}

.detail-damage-graph i {
    z-index: 1;
    display: block;
    position: absolute;
    top: 0; left: 0;
    width: 50%;
    height: 100%;
    background: #ed6767;
}

.detail-items {
    align-items: center;
}

.detail-items-wrap {
    display: flex;
}

.detail-item-list {
    display: flex;
    width: 20px;
    height: 20px;
    margin-right: 2px;
}

.detail-item-list:last-child {
    margin-right: 0px;
}

.detail-item-list-wrap {
    width: 100%;
    height: 100%;
    background: #e6e6e6;
}

.detail-item-list-wrap img {
    width: 100%;
}

</style>