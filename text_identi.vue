<template>
    <div class="text_identi_contianer">
        <div class="text_analyze">
            <div class="text_analyze_holder">请输入文本信息</div>
            <el-input
                v-model="textinfo"
                :rows="15"
                type="textarea"
                placeholder="请输入需要分析的文本信息"
            />
            <div class="text_analyze_btns">
                <el-button type="primary">开始分析</el-button>
                <el-button type="primary">作者画像</el-button>
                <el-button type="primary" @click="getResult">文本结果</el-button>
            </div>
        </div>
    </div>
    <textIdentiDetial :visible='detialVisible' :info='detailInfo' @close='detialVisible=false'></textIdentiDetial>
</template>

<script>
import textIdentiDetial from '../components/text_identi_detial.vue'

export default {
    name: 'text_identi',
    components: {
        textIdentiDetial: textIdentiDetial
    },
    emits: ['routeSwitch'],
    data() {
        return {
            textinfo: "几个少年辛苦奔走了十多年，暗地里一颗弹丸要了他的性命；几个少年一击不中，在监牢里身受一个多月的苦刑；几个少年怀着远志，忽然踪影全无，连尸首也不知那里去了。——“他们都在社会的冷笑恶骂迫害倾陷里过了一生；现在他们的坟墓也早在忘却里渐渐平塌下去了。",
            detialVisible: false,
            detailInfo: {}
        }
    },
    methods: {
        getResult() {
            this.detailInfo = {
                id: 10,
                text: this.textinfo,
                date: '2021-12-25'
            }
            this.detialVisible = true
        }
    },
    created() {
        this.$emit('routeSwitch', this.$route)
    }
}
</script>

<style scoped>
.text_identi_contianer {
    height: 100%;
}
.text_analyze_holder {
    font-size: 18px;
    margin-bottom: 10px;
}
.text_analyze_btns {
    margin: 10px 0;
}
</style>