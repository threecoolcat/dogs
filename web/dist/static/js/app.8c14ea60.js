(function(t){function e(e){for(var l,o,i=e[0],u=e[1],c=e[2],p=0,d=[];p<i.length;p++)o=i[p],Object.prototype.hasOwnProperty.call(n,o)&&n[o]&&d.push(n[o][0]),n[o]=0;for(l in u)Object.prototype.hasOwnProperty.call(u,l)&&(t[l]=u[l]);s&&s(e);while(d.length)d.shift()();return a.push.apply(a,c||[]),r()}function r(){for(var t,e=0;e<a.length;e++){for(var r=a[e],l=!0,i=1;i<r.length;i++){var u=r[i];0!==n[u]&&(l=!1)}l&&(a.splice(e--,1),t=o(o.s=r[0]))}return t}var l={},n={app:0},a=[];function o(e){if(l[e])return l[e].exports;var r=l[e]={i:e,l:!1,exports:{}};return t[e].call(r.exports,r,r.exports,o),r.l=!0,r.exports}o.m=t,o.c=l,o.d=function(t,e,r){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:r})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var r=Object.create(null);if(o.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var l in t)o.d(r,l,function(e){return t[e]}.bind(null,l));return r},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],u=i.push.bind(i);i.push=e,i=i.slice();for(var c=0;c<i.length;c++)e(i[c]);var s=u;a.push([0,"chunk-vendors"]),r()})({0:function(t,e,r){t.exports=r("56d7")},"034f":function(t,e,r){"use strict";var l=r("85ec"),n=r.n(l);n.a},"50e9":function(t,e,r){"use strict";var l=r("90b4"),n=r.n(l);n.a},"56d7":function(t,e,r){"use strict";r.r(e);r("e260"),r("e6cf"),r("cca6"),r("a79d");var l=r("2b0e"),n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{attrs:{id:"app"}},[r("HelloWorld",{attrs:{msg:"Welcome to Your Vue.js App"}})],1)},a=[],o=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("el-row",[r("el-col",{attrs:{gutter:20}},[r("el-card",{staticClass:"box-card"},[r("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[r("span",[t._v("主订单")])]),r("div",[r("el-table",{attrs:{data:t.mainList,border:"",strip:"","highlight-current-row":""},on:{"row-click":t.loadDetail}},[r("el-table-column",{attrs:{label:"采购单号",prop:"id"}}),r("el-table-column",{attrs:{label:"采购单名称",prop:"title"}}),r("el-table-column",{attrs:{label:"采购员",prop:"buyer"}}),r("el-table-column",{attrs:{label:"供货商",prop:"supplier"}}),r("el-table-column",{attrs:{label:"联系电话",prop:"call"}}),r("el-table-column",{scopedSlots:t._u([{key:"default",fn:function(e){return[r("el-button",{attrs:{size:"mini",type:"text"},on:{click:function(r){return t.loadDetail(e.row)}}},[t._v("查看明细")])]}}])})],1)],1)])],1)],1),r("el-divider"),r("el-row",[r("el-col",{attrs:{gutter:20}},[r("el-card",{staticClass:"box-card"},[r("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[r("span",[t._v("采购单明细:"+t._s(t.currentM.title))])]),r("div",[t.detailList.length>0?r("el-table",{attrs:{data:t.detailList,border:"",strip:""}},[r("el-table-column",{attrs:{label:"采购单号",prop:"Mid"}}),r("el-table-column",{attrs:{label:"顺序号",prop:"id"}}),r("el-table-column",{attrs:{label:"采购水果名称",prop:"name"}}),r("el-table-column",{attrs:{label:"采购数量",prop:"number"}}),r("el-table-column",{attrs:{label:"单位",prop:"unit"}}),r("el-table-column",{attrs:{label:"单价",prop:"price"}})],1):t._e()],1)])],1)],1)],1)},i=[],u=r("bc3a"),c=r.n(u),s={name:"HelloWorld",props:{msg:String},data:function(){return{mainList:[],detailList:[],currentM:{}}},created:function(){this.loadMain()},methods:{loadMain:function(){var t=this;c.a.get("http://127.0.0.1:8000/main",{}).then((function(e){t.mainList=e.data}))},loadDetail:function(t,e,r){var l=this;this.currentM=t,c.a.get("http://127.0.0.1:8000/detail",{params:{Mid:t.id}}).then((function(t){l.detailList=t.data}))}}},p=s,d=(r("50e9"),r("2877")),f=Object(d["a"])(p,o,i,!1,null,"0d11f432",null),b=f.exports,m={name:"App",components:{HelloWorld:b}},h=m,v=(r("034f"),Object(d["a"])(h,n,a,!1,null,null,null)),g=v.exports,y=r("5c96"),w=r.n(y);r("0fae");l["default"].use(w.a),l["default"].config.productionTip=!1,new l["default"]({render:function(t){return t(g)}}).$mount("#app")},"85ec":function(t,e,r){},"90b4":function(t,e,r){}});