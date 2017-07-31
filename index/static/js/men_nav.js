$(function(){
	/////////////点击导航显示二级导航

	/////////////////
   var _width = $(window).width();
	if(_width > 1600){
		 $(".er01").css({"left":"102px"})
		 $(".er02").css({"left":"204px"})
		 $(".er03").css({"left":"306px"})
		 $(".er04").css({"left":"306px"})
		 $(".er05").css({"left":"408px"})
         $(".er06").css({"left":"510px"})
	 }else if(_width <= 1600 && _width>1024){
		 $(".er01").css({"left":"72px"})
		 $(".er02").css({"left":"144px"})
		 $(".er03").css({"left":"216px"})
		 $(".er04").css({"left":"216px"})
		 $(".er05").css({"left":"288px"})
         $(".er06").css({"left":"360px"})
	 }else if(_width <= 1024){
	 	 $(".navBtn").click(function(){
	 	 	$(".down").toggle();
		 })

		 $(".er01").css({"left":"70px","top":"48px"})
		 $(".er02").css({"left":"70px","top":"94px"})
		 $(".er03").css({"left":"70px","top":"140px"})
		 $(".er04").css({"left":"70px","top":"188px"})
		 $(".er05").css({"left":"70px","top":"234px"})
         $(".er06").css({"left":"70px","top":"284px"})
	 }
})