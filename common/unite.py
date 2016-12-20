# -*- coding:utf-8 -*-
"""
@Created Time：2016/12/15

@author：HAO
"""
from requests import session
from bs4 import BeautifulSoup

# cookies = {'sheyuan_flowapi_app_h5_auth': "0e07a34f8f814b8594c9860fe20be51a"}
#
html = """
<!DOCTYPE html>

<html>

<head lang="en">

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0"/>

<title>下单付款页</title>

<link rel="stylesheet" href="https://syhapp.sheyuan.com:443/css/reset.css"/>

<link rel="stylesheet" href="https://syhapp.sheyuan.com:443/css/orderConfirmBase.css"/>

<link rel="stylesheet" href="https://syhapp.sheyuan.com:443/css/orderConfirm.css"/>

<script src="https://syhapp.sheyuan.com:443/js/jquery-2.1.1.min.js"></script>

<script src="https://syhapp.sheyuan.com:443/js/autoWidth.js"></script>

</head>

<style>

html{font-size:100px;}

a{

color: #333;

}

.xj{

overflow: hidden;

height:auto;

background:#FFFFFF;

position:fixed;

z-index: 101;

top:50%;

left:50%;

margin-left:-3.2rem;

margin-top:-1rem;

line-height:.62rem;

}

.xj dl{

width: 6.4rem;

padding: 0.1rem 0.1rem;

overflow: hidden;

border: 1px solid #e5e5e5;

}

.cp{

float: left;

width: 1rem;

height: 1rem;

border: 1px solid #e1e1e1;

border-radius: 2px;

}

.xj dl dt{

/* float:left;

width: 3.34rem;

height: .94rem;*/

/* line-height: 0.42rem;*/

overflow: hidden;

color: #434343;

font-size: 0.28rem;

margin-left:.2rem;

padding-left:.2rem;

}

.xj dl dd{

/* float:right;

width:auto;

height: 0.9rem;*/

font-size:.24rem;

/* line-height: 0.9rem;*/

overflow: hidden;

padding-left:.2rem;

}

.xj p{

padding: 0 0.1rem;

width: 6.4rem;

height:.6rem;

line-height:.6rem;

font-size:.28rem;

border:1px solid #e5e5e5;

text-align:center;

border-bottom:none;

}

</style>

<body>

<!--主体布局容器-->

<div class="layout">

<form action="https://syhapp.sheyuan.com:443/order/createOrder" method="post" id="createOrder" target="_self">

<div class="top">

<a href="javascript:returnBack();"><span id="returnBtn"><img src="https://syhapp.sheyuan.com:443/images/return.png" alt=""/></span></a>

确认订单

</div>

<div style="height:0.88rem"></div>

<a href="https://syhapp.sheyuan.com:443/addr/addrList">

<div class="dizhi">

<div class="dizhi-1">

<div class="shouhuoren">收货人：张浩</div>

<div class="dianhua">18600231840</div>

</div>

<div class="dizhi-1" style="margin-left:2%;clear: both;height:auto;margin-left: 0;">

<img style="float: left;width: 5%;"src="https://syhapp.sheyuan.com:443/img/order/5.png.gif">

<div style="padding-bottom: 0.5rem;font-size: 0.3rem; width:90%;margin-left:4%;line-height: 0.59rem;float: left;

">北京 北京 朝阳望京SOHO塔1A座</div>

</div>

</div>

</a>

<div class="tupian-1"></div>

<div class="beijing-1"></div>

<div class="shanyao">

<a href="javascript:toCelebrity(231)"><div class="shanyao-top">

<div class="nvshen"><img src="http://syimg.sheyuan.com/userheadpic/default_head1.png"></div>

<span>刘洪贵</span>

</div><a>

<a href="javascript:toGoodsDetail(26)"><div class="pingguo">

<div class="tupian"><img class="shangpin" src="http://syimg.sheyuan.com/img07/13940237582-1.jpg" alt="" /></div>

<div class="wenzi">葡萄</div>

<div class="jiage">

<div>重量：5斤</div>

<div>

<span class="fl">X1</span>

<span class="ri yanse">¥155.00</span>

</div>

</div>

</div>

</a>

<div class="beijing-1"></div>

<a href="https://syhapp.sheyuan.com:443/coupon/selectCoupon?key=cart_info_ac6042ea-f74a-48c1-84b6-add0cb647675">

<div class="youhuiquan">

<span class="youhuiquan-l">优惠券</span>

<span class="youhuiquan-2">已优惠0.00元</span>

<img src="https://syhapp.sheyuan.com:443/img/order/youhuiquantb.png">

<span class="youhuiquan-3">暂无可用,<i style='color:blue;font-style:normal;'>绑定</i></span>

</div>

</a>

<div class="beijing-1"></div>

<div class="dingdanzonge">

<div class="dingdanzonge-1">

<div class="dingdanzonge-1-top fl">商品总额</div>

<div class="dingdanzonge-1-bom ri">¥155.00</div>

</div>

<div class="dingdanzonge-2">

<div class="dingdanzonge-1-top fl">优惠</div>

<div class="dingdanzonge-1-bom ri">-¥0.00</div>

</div>

<div class="dingdanzonge-2">

<div class="dingdanzonge-1-top fl">运费</div>

<div class="dingdanzonge-1-bom ri">¥0.00</div>

</div>

</div>

<input type="hidden" id="addrId" name="addrId" value="581dc10af28d7462f6f9f43a" />

<input type="hidden" name="totalAmount" value="155.00">

<input type="hidden" name="shipPrice" value="0.00">

<input type="hidden" name="couponAmount" value="0.00">

<input type="hidden" id="couponId" name="couponId" value="">

<input type="hidden" name="payAmount" value="155.00">

<input type="hidden" id="ids" name="ids" value="5043">

<div style="width:100%;height:1rem;overflow:hidden;"></div>

<div class="guding">

<div class="shifukuan">

<div class="shifukuan-1">合计：<span>155.00</span></div>

<a href="javascript:createOrder()"><div class="querentijiao ri">提交订单</div></a>

</div>

</div>

</div>

</form>

</div>

<div class="ceng"></div>

<div class="xj" id="message" style="display:none;">

</div>

</body>

<script>

$(function () {

// 创建订单

/*$("#createOrderBtn").click(function () {

createOrder()

})*/

});

function returnBack(){

var buyNow = 1;

if(1==buyNow){

finish(26);

}else{

window.location.href = 'https://syhapp.sheyuan.com:443/goodsCart/goodsList';

}

/* var buyNow = 1;

if(1==buyNow){

finish(26);

}else{

//history.go(-1);

window.location.href = document.referrer;

} */

}

// 创建订单

var flag = 0;

function createOrder(){

if(flag == 0){

flag = 1;

var addrId = $("#addrId").val();

if(null == addrId || "" == addrId.trim()){

$("#message").text("");

$("#message").append("<dl><dt style='line-height: 0.9rem;'>请先添加收货人地址！</dt></dl>");

$(".xj").show(300).delay(3000).hide(300);

flag = 0;

return false;

}

var ids = $("#ids").val();

var couponId = $("#couponId").val();

$.post("https://syhapp.sheyuan.com:443//order/createOrder",{'ids':ids,'addrId':addrId,'couponId':couponId},function(data){

if(data){

var result = JSON.parse(data);

if(10801==result.flag || 10901==result.flag){

$("#message").text("");

$("#message").append("<dl><dt style='line-height: 0.9rem;'>"+result.mess+"</dt></dl>");

$(".xj").show(300).delay(3000).hide(300);

return false;

}

if(10716==result.flag || 10717==result.flag){

$("#message").text("");

var html = '';

html += '<p>'+result.mess+'</p>';

for(var i=0;i<result.goodsList.length;i++) {

var item = result.goodsList[i];

html += '<dl>';

html += ' <img class="cp" src="'+item.photoUrlPage+'" alt="" />';

html += ' <dt>'+item.goodsName+'</dt>';

html += ' <dd>';

if(null == item.specDesc || "undefined"==item.specDesc){

html += ' 重量：';

}else{

html += ' 重量：'+item.specDesc;

}

html += '斤 </dd>';

html += '</dl>';

}

$("#message").append(html);

$(".xj").show(300).delay(3000).hide(300);

$("#createOrderBtn").attr("disabled","disabled");

flag = 0;

return false;

}else if(0==result.flag){

window.location.href='https://syhapp.sheyuan.com:443//pay/orderPay?orderId='+result.orderId;

//jQuery("#createOrder").submit();

}else{

return false;

}

}else{

return false;

}

},"text");

}

}

</script>

<script>

function toCelebrity(id){

if ("undefined" != typeof jsAndroid) {

window.jsAndroid.toCelebrity(id);

}else{

connectWebViewJavascriptBridge(function(bridge) {

/* IOS */

bridge.callHandler('toCelebrity', {'id':id}, function(response) {});

})

}

}

function toGoodsDetail(id){

if ("undefined" != typeof jsAndroid) {

window.jsAndroid.toGoodsDetail(id);

}else{

connectWebViewJavascriptBridge(function(bridge) {

/* IOS */

bridge.callHandler('toGoodsDetail', {'id':id}, function(response) {});

})

}

}

function finish(id){

if ("undefined" != typeof jsAndroid) {

window.jsAndroid.finish();

}else{

connectWebViewJavascriptBridge(function(bridge) {

// IOS

bridge.callHandler('toBack', {'toBack':true}, function(response) {});

})

/*connectWebViewJavascriptBridge(function(bridge) {

bridge.callHandler('toGoodsDetail', {'id':id}, function(response) {});

})*/

}

}

/*IOS */

function connectWebViewJavascriptBridge(callback) {

if (window.WebViewJavascriptBridge) {

callback(WebViewJavascriptBridge);

} else {

document.addEventListener('WebViewJavascriptBridgeReady', function() {callback(WebViewJavascriptBridge);}, false);

}

}

</script>

</html>
"""
import re

a = """<input type="hidden" id="addrId" name="addrId" value="(.+)" />userToken=$TEST01_{$.modelData.userToken}&goodsId=$TEST03_{$.modelData.result[0].productId}&evaluateNum=1&os=android&version=3.0"""


reg = """["'](.[^:"']+?)["']\s*:\s*["']\$(.+?)_\{(.+?)\}"""
result_list = re.findall(reg, str(a))
print(result_list)