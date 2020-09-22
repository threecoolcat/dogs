<template>
  <div>
    <el-row>
      <el-col :gutter="20">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>主订单</span>
          </div>
          <div>
            <el-table :data="mainList" border strip highlight-current-row @row-click="loadDetail">
              <el-table-column label="采购单号" prop="id" />
              <el-table-column label="采购单名称" prop="title" />
              <el-table-column label="采购员" prop="buyer" />
              <el-table-column label="供货商" prop="supplier" />
              <el-table-column label="联系电话" prop="call" />
              <el-table-column>
                <template slot-scope="scope">
                  <el-button size="mini" type="text" @click="loadDetail(scope.row)">查看明细</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-divider/>
    <el-row>
      <el-col :gutter="20">
        <el-card class="box-card" >
          <div slot="header" class="clearfix">
            <span>采购单明细:{{currentM.title}}</span>
          </div>
          <div>
            <el-table :data="detailList" border strip v-if="detailList.length > 0">
              <el-table-column label="采购单号" prop="Mid" />
              <el-table-column label="顺序号" prop="id" />
              <el-table-column label="采购水果名称" prop="name" />
              <el-table-column label="采购数量" prop="number" />
              <el-table-column label="单位" prop="unit" />
              <el-table-column label="单价" prop="price" />
              
            </el-table>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String

  },
  data() {
      return {
        mainList: [],
        detailList: [],
        currentM: {}
      }
  },
  //加载方法
  created() {
    this.loadMain()
    // this.loadDetail()
  },
  //方法定义
  methods: {
    loadMain() {
        axios.get('http://127.0.0.1:8000/main', {}).then(resp=>{
            // console.log('main', resp)
            this.mainList = resp.data;
        })
    },

    loadDetail(row, col, e) {
      this.currentM = row;
      axios.get('http://127.0.0.1:8000/detail', {params: {Mid: row.id}}).then(resp=>{
          // console.log('detail',resp)
          this.detailList = resp.data;
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
