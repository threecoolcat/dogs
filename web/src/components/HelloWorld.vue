<template>
  <div>
    <el-row>{{ msg }}</el-row>
    <el-divider/>
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="订单演示" name="first">
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
      </el-tab-pane>
      <el-tab-pane label="AES加密演示" name="second">
        <el-row>
          <el-col :span="4">
            密钥
          </el-col>
          <el-col :span="10">
            <el-input v-model="key" readonly/>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="4">内容</el-col>
          <el-col :span="10">
            <el-input v-model="text" />
            
          </el-col>
          <el-col :span="4">
            <el-button @click="clickEncrypt">加密</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="4">密文</el-col>
          <el-col :span="10">
            <el-input v-model="encryptedText" />
          </el-col>
          <el-col :span="4">
            <el-button @click="clickSendToServer">发送到服务器</el-button>
          </el-col>
        </el-row>
      </el-tab-pane>
    </el-tabs>
    
  </div>
</template>

<script>
import qs from 'qs'
import axios from 'axios'
import CryptoJS from 'crypto-js'
export default {
  name: 'HelloWorld',
  props: {
    msg: String

  },
  data() {
      return {
        activeName: 'first',
        key: '1234567890123456',  //密钥必须是16个字符，如果密钥不足16个字符，请自行补齐
        text: '这是一段需要加密的文本，服务器上需要解密才能查看',
        encryptedText: '',
        mainList: [],
        detailList: [],
        currentM: {},

      }
  },
  //加载方法
  created() {
    this.loadMain()
    // this.loadDetail()
  },
  //方法定义
  methods: {
    clickEncrypt(){
      this.encryptedText = this.encrypt(this.text, this.key)
    },
    clickSendToServer() {
      this.clickEncrypt()
      axios.post('http://127.0.0.1:8000/decode/', qs.stringify({data: this.encryptedText})).then(resp=>{
        console.log(resp)
        this.$alert(resp.data);
      })
    },
    loadMain() {
        axios.get('http://127.0.0.1:8000/main/', {}).then(resp=>{
            // console.log('main', resp)
            this.mainList = resp.data;
        })
    },

    loadDetail(row) {
      this.currentM = row;
      axios.get('http://127.0.0.1:8000/detail/', {params: {Mid: row.id}}).then(resp=>{
          // console.log('detail',resp)
          this.detailList = resp.data;
      })
    },
    // 加密
    encrypt(word, keyStr){ 
      keyStr = keyStr ? keyStr : this.key;
      var key  = CryptoJS.enc.Utf8.parse(keyStr);//Latin1 w8m31+Yy/Nw6thPsMpO5fg==
      var srcs = CryptoJS.enc.Utf8.parse(word);
      var encrypted = CryptoJS.AES.encrypt(srcs, key, {mode:CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7});
      return encrypted.toString();
    },
    // 解密
    // 本演示中，js端只负责加密， 不使用解密方法， 请在django端查看解密方法
    // decrypt(word, keyStr){  
    //   keyStr = keyStr ? keyStr : this.key;
    //   var key  = CryptoJS.enc.Utf8.parse(keyStr);//Latin1 w8m31+Yy/Nw6thPsMpO5fg==
    //   var decrypt = CryptoJS.AES.decrypt(word, key, {mode:CryptoJS.mode.ECB,padding: CryptoJS.pad.Pkcs7});
    //   return CryptoJS.enc.Utf8.stringify(decrypt).toString();
    // }
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
