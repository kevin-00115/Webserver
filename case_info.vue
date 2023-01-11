<template>
    <div class="text_hist_container">
        <div class="text_hist_head">
            事件信息
        </div>
        <div class="text_hist_table">
            <el-table :data="tabelData" border>
                <el-table-column prop="id" label="案件编号" width="100"></el-table-column>
                <el-table-column prop="text" label="文本"></el-table-column>
                <el-table-column prop="author" label="作者" width="100"></el-table-column>
                <el-table-column prop="date" label="日期" width="105"></el-table-column>
                <el-table-column prop="opt" label="操作" width="100">
                    <template v-slot="scope">
                        <div class="text_hist_table_opt">
                        <el-link type="primary" @click="getDetial(scope.row)">查看详情</el-link>
                        </div>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div class="text_hist_footer">
            <el-pagination
            layout="prev, pager, next"
            :total="1000">
        </el-pagination>
        </div>
    </div>
    <textIdentiDetial :visible='detialVisible' :info='detailInfo' @close='closeDetail'></textIdentiDetial>
</template>

<script>
import textIdentiDetial from '../components/text_identi_detial.vue'
export default {
    name: "case_info",
    components: {
        textIdentiDetial: textIdentiDetial
    },
    data() {
        return {
            tabelData: [
                {
                    id: 0,
                    text: '几个少年辛苦奔走了十多年，暗地里一颗弹丸要了他的性命；几个少年一击不中，在监牢里身受一个多月的苦刑；几个少年怀着远志，忽然踪影全无，连尸首也不知那里去了。——“他们都在社会的冷笑恶骂迫害倾陷里过了一生；现在他们的坟墓也早在忘却里渐渐平塌下去了。',
                    author: 'liuben',
                    date: '2022-01-07'
                },
                {
                    id: 1,
                    text: '他，——怎样？“他？母亲说着，便向房外看，“这些人又来了。说是买木器，顺手也就随便拿走的，我得去看看。母亲站起身，出去了。门外有几个女人的声音。我便招宏儿走近面前，和他闲话：问他可会写字，可愿意出门。“我们坐火车去么？',
                    author: 'liuben',
                    date: '2022-01-07'
                },
                {
                    id: '2',
                    text: '我们日里到海边捡贝壳去，红的绿的都有，鬼见怕也有，观音手⑸也有。晚上我和爹管西瓜去，你也去。“管贼么？“不是。走路的人口渴了摘一个瓜吃，我们这里是不算偷的。要管的是獾猪，刺猬，猹。月亮底下，你听，啦啦的响了，猹在咬瓜了。',
                    author: 'liuben',
                    date: "2022-01-03"
                },
                {
                    id: '3',
                    text: '天气还早，何家已经坐着四个病人了。他摸出四角银元，买了号签，第五个轮到宝儿。何小仙伸开两个指头按脉，指甲足有四寸多长，单四嫂子暗地纳罕，心里计算：宝儿该有活命了。但总免不了着急，忍不住要问，便局局促促的说：“先生，——我家的宝儿什么病呀？',
                    author: 'liuben',
                    date: "2021-11-23"
                },
                {
                    id: '4',
                    text: '现在不知他唯一的女儿景况如何？倘在上学，中学已该毕业了罢。我总要上下四方寻求，得到一种最黑，最黑，最黑的咒文，先来诅咒一切反对白话，妨害白话者。即使人死了真有灵魂，因这最恶的心，应该堕入地狱，也将决不改悔，总要先来诅咒一切反对白话，妨害白话者。',
                    author: 'liuben',
                    date: "2021-12-30"
                },
                {
                    id: '5',
                    text: '虽然从来如此，我们今天也可以格外要好，说是不能！大哥，我相信你能说，前天佃户要减租，你说过不能。当初，他还只是冷笑，随后眼光便凶狠起来，一到说破他们的隐情，那就满脸都变成青色了。大门外立着一伙人，赵贵翁和他的狗，也在里面，都探头探脑的挨进来。',
                    author: 'liuben',
                    date: "2021-12-24"
                },
                {
                    id: '6',
                    text: '“我什么时候跳进你的园里来偷萝卜？阿Q且看且走的说。“现在……',
                    author: 'liuben',
                    date: "2022-01-01"
               }
            ],
            detialVisible: false,
            detailInfo: {}
        }
    },
    emits: ['routeSwitch'],
    methods: {
        getDetial(row) {
            this.detailInfo = row
            this.detialVisible = true
        },
        closeDetail(){
            this.detialVisible = false
        }
    },
    created() {
        this.$emit('routeSwitch', this.$route)
    }
}
</script>

<style>
.text_hist_container {
    height: 100%;
}
.text_hist_table {
    margin-top: 12px;
    /* max-height: 70%; */
    overflow: scroll;
}
.text_hist_footer {
    margin-top: 12px;
}
</style>