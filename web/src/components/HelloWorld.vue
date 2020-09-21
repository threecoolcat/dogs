<template>
  <div>
  主订单
    <ul style="list-style-type: list;">
       <li style="border:1px solid #bbb; padding:4px;display:block"
           v-for="item in mainList"
           :key="item.id">
         title:{{item.title}}, buyer: {{item.buyer}}
       </li>
    </ul>
    订单明细
    <ul>
       <li style="border:1px solid #ccc; padding:4px;display:block"
           v-for="item in detailList"
           :key="item.id">
         name:{{item.name}}, number: {{item.number}}
       </li>
    </ul>
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
        detailList: []
      }
  },
  //加载方法
  created() {
    this.loadMain()
    this.loadDetail()
  },
  //方法定义
  methods: {
    loadMain() {
        axios.get('http://127.0.0.1:8000/main', {}).then(resp=>{
            // console.log('main', resp)
            this.mainList = resp.data;
        })
    },
    loadDetail() {
        axios.get('http://127.0.0.1:8000/detail', {}).then(resp=>{
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
