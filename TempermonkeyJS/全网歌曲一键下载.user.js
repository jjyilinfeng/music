// ==UserScript==
// @name         全网歌曲一键下载
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        *://music.163.com/*
// @match        *://y.qq.com/n/yqq/song/*
// @match        *://www.kugou.com/*
// @match        *://www.kuwo.cn/*
// @match        *://www.xiami.com/*
// @match        *://music.baidu.com/*
// @match        *://www.qingting.fm/*
// @match        *://www.lizhi.fm/*
// @match        *://music.migu.cn/*
// @match        *://www.ximalaya.com/*
// @match        *://192.168.31.30:8000/home/index/*
// @grant        unsafeWindow
// @require      http://cdn.bootcss.com/jquery/1.8.3/jquery.min.js
// @icon         http://music.sonimei.cn/favicon.ico
// @run-at       document-end
// ==/UserScript==

(function() {
    'use strict';
     var curPlaySite = '';
	var curWords = '';
	var videoSite = window.location.href;
	var reWY = /163(.*)song/i;
	var reQQ = /QQ(.*)song/i;
	var reKG = /kugou(.*)song/i;
	var reKW = /kuwo(.*)yinyue/i;
	var reXM = /xiami/i;
	var reBD = /baidu/i;
	var reQT = /qingting/i;
	var reLZ = /lizhi/i;
	var reMG = /migu/i;
	var reXMLY = /ximalaya/i;
	var vipBtn = '<a target="_blank" id="VipMusicBtn" style="margin:10px 0;display:inline-block;padding:0 5px;height:22px;border:1px solid red;color:red;vertical-align:bottom;text-decoration:none;font-size:17px;line-height:22px;cursor:pointer;">一键免费下载</a>';
    var Url =  decodeURIComponent(window.location.href)
    var user_ip = "192.168.31.30"
    var values = {
  search_music_url:Url.replace('http://'+user_ip+':8000/home/index/?url=',"")
};
  //网易云音乐
  if(reWY.test(videoSite)){
    var Title = $('.u-icn-37');
    Title.parent('.hd').after(vipBtn);
    $('#VipMusicBtn').attr('href','http://'+user_ip+':8000/home/index/?url=' + window.location.href);
      
  }


  //QQ音乐
  if(reQQ.test(videoSite)){
    var Title = $('.data__name_txt');
    Title.parent('.data__name').after(vipBtn);
    $('#VipMusicBtn').attr('href','http://'+user_ip+':8000/home/index/?url=' + window.location.href);
  }

      //酷狗音乐
  if(reKG.test(videoSite)){
	KGadd();
	setInterval(function(){KGadd()},1000);
	function KGadd(){
		if($("#VipMusicBtn").length==0 && $(".audioName").length>0){
			var Title = $('.audioName');
			Title.parent('.songName').after(vipBtn);
		}
		$("#VipMusicBtn").attr("href",'http://'+user_ip+':8000/home/index/?url=' + window.location.href);
	}
  }

      //荔枝FM
  if(reLZ.test(videoSite)){
    var Title = $('.audioName');
    Title.parent('.audioInfo').after(vipBtn);
    $('#VipMusicBtn').attr('href','http://'+user_ip+':8000/home/index/?url=' + window.location.href);
  }

      //百度音乐
  if(reBD.test(videoSite)){
    var Title = $('.songpage-title');
    Title.parent('.song').after(vipBtn);
    $('#VipMusicBtn').attr('href','http://'+user_ip+':8000/home/index/?url=' + window.location.href);
  }

     Object.keys(values).forEach(function(key){
    $("#" + key).val(values[key]);
  });
})();
