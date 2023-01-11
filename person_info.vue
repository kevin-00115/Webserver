<template>
    <div>人员信息</div>
    <div class="label_tabel">
        <el-table :data="labelTable" border >
            <el-table-column prop="label" label="标签" width="120"></el-table-column>
            <el-table-column prop="feature" label="特征"></el-table-column>
            <el-table-column prop="opt" label="操作" width="100">
                <template v-slot="scope">
                    <el-link type="primary" @click="addFeature(scope.row)">新增特征</el-link>
                </template>
            </el-table-column>
        </el-table>
    </div>
    <el-button type="primary" style="width: 100px" @click="addLabel">新增标签</el-button>
    <el-dialog v-model="digVis"
        :title="detialRow.flag==0 ? '新增特征':'新增标签'"
    >
        <div v-if="detialRow.flag==0" class="add_dialog_div">
            <div class="exit_label_feature">
                <span>{{detialRow.label}}: </span>
                <span>{{detialRow.feature}}</span>
            </div>
            <div class="new_label_feature">
                <span>请输入新增特征:</span>
                <el-input
                placeholder="请输入特征"
                v-model="addInput"
                clearable>
                </el-input>
            </div>
        </div>
        <div v-else class="add_dialog_div">
            <div class="new_label_feature">
                <span>请输入新增标签:</span>
                <el-input
                placeholder="请输入特征"
                v-model="addInput"
                clearable>
                </el-input>
            </div>
        </div>
        <el-button type="primary" size="mini" @click="addLabel">提交</el-button>
        <el-button type="primary" size="mini" @click="digVis=false">关闭</el-button>
    </el-dialog>
</template>

import axios from 'axios';
<script>
import axios from "axios";

export default {
    "name": "person_info",
    "components": {},
    "data"() {
        return {
            "labelTable": [
                {
                    "label": '姓名',
                    "feature": '刘犇'
                },
                {
                    "label": '地域',
                    "feature": '上海，杭州，南京'
                },
                {
                    "label": '年龄',
                    "feature": '-'
                },
                {
                    "label": '性别',
                    "feature": '男，女'
                },
                {
                    "label": '文化程度',
                    "feature": '初中，高中，大专，本科'
                },
                {
                    "label": '职业群体',
                    "feature": 'IT，无业'
                },
                {
                    "label": '病态',
                    "feature": '狂躁症，抑郁症'
                },
            ],
            "detialRow": {},
            "digVis": false,
            "addInput": ''
        }
    },
    "methods": {
      "addFeature": async function (row) {
        console.log("hello2")
        this.detialRow = row;
        this.detialRow.flag = 0;
        this.digVis = true;
        try {
          const response = await axios.post(
              "api/add_feature/",
              {"name": this.addInput, "label": row.label.id}
          );
          console.log(response.data);
        } catch (error){
          console.log(error);
        }
      },
      async "addLabel"() {
        console.log("hello")
        this.detialRow = {}
        this.detialRow.flag = 1
        this.digVis = true
        try {
          const response = await axios.post("api/add_label/",
              {
              "name": this.addInput});
          this.labelTable.push(response);
          this.addInput = '';
          console.log('2')
          console.log(response.data);
        } catch (error) {
          console.log(error)
        }
      },
    },
  emits: {
      'routeSwitch': '',
  },
    "created"() {
        this.$emit('routeSwitch', this.$route,)
    },
}
</script>

<style>
.label_tabel {
    flex: 1;
    margin: 12px 0;
}
.add_dialog_div {
    margin-bottom: 10px;
}
.exit_label_feature {
    font-size: 18px;
    margin-bottom: 12px;
}
.new_label_feature {
    /* display: flex;
    justify-content: center;
    align-items: center; */
}
.new_label_feature span {
    /* word-break: keep-all; */
}
</style>

