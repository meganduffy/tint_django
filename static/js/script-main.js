// NAVBAR ANIMATION
$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar-fixed-top");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});

//TRANSCRIPT TRACKER TOGGLE FULL DETAILS
function showFullDetails() {
    var x = document.getElementById('full-details');
    if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }

}

// ABOUT CLICK AND REVEAL
$(document).ready(function()
{
		"use strict";
		//btn1
		$("#about-2-icon-1").click(function(){
			$("#about-2-icon-2, #about-2-icon-3, #about-2-icon-4, #about-2-icon-5, #about-2-icon-6").removeClass("active-box");
			$( this ).addClass("active-box");
			$(".about-2-icon-box").removeClass("active-item");
			$("#ih1").addClass("active-item");
			$("#about-info-2, #about-info-3, #about-info-4, #about-info-5, #about-info-6").hide();
			$("#about-info-default").fadeIn(450).css({"display":"flex"});
		});
		//btn2
		$("#about-2-icon-2").click(function(){
			$("#about-2-icon-1, #about-2-icon-3, #about-2-icon-4, #about-2-icon-5, #about-2-icon-6").removeClass("active-box");
			$( this ).addClass("active-box");
			$(".about-2-icon-box").removeClass("active-item");
			$("#ih2").addClass("active-item");
			$("#about-info-default, #about-info-3, #about-info-4, #about-info-5, #about-info-6").hide();
			$("#about-info-2").fadeIn(450).css({"display":"flex"});
		});
		//btn3
		$("#about-2-icon-3").click(function(){
			$("#about-2-icon-1, #about-2-icon-2, #about-2-icon-4, #about-2-icon-5, #about-2-icon-6").removeClass("active-box");
			$( this ).addClass("active-box");
			$(".about-2-icon-box").removeClass("active-item");
			$("#ih3").addClass("active-item");
			$("#about-info-default").hide();
			$("#about-info-2").fadeIn(150).css({"display":"flex"});
			$("#about-info-default, #about-info-2, #about-info-4, #about-info-5, #about-info-6").hide();
			$("#about-info-3").fadeIn(450).css({"display":"flex"});
		});
		//btn4
		$("#about-2-icon-4").click(function(){
			$("#about-2-icon-1, #about-2-icon-3, #about-2-icon-2, #about-2-icon-5, #about-2-icon-6").removeClass("active-box");
			$( this ).addClass("active-box");
			$(".about-2-icon-box").removeClass("active-item");
			$("#ih4").addClass("active-item");
			$("#about-info-default, #about-info-3, #about-info-2, #about-info-5, #about-info-6").hide();
			$("#about-info-4").fadeIn(450).css({"display":"flex"});
		});
		//btn5
		$("#about-2-icon-5").click(function(){
			$("#about-2-icon-1, #about-2-icon-3, #about-2-icon-4, #about-2-icon-2, #about-2-icon-6").removeClass("active-box");
			$( this ).addClass("active-box");
			$(".about-2-icon-box").removeClass("active-item");
			$("#ih5").addClass("active-item");
			$("#about-info-default, #about-info-3, #about-info-4, #about-info-2, #about-info-6").hide();
			$("#about-info-5").fadeIn(450).css({"display":"flex"});

		});
		//btn6
		$("#about-2-icon-6").click(function(){
			$("#about-2-icon-1, #about-2-icon-3, #about-2-icon-4, #about-2-icon-5, #about-2-icon-2").removeClass("active-box");
			$( this ).addClass("active-box");
			$(".about-2-icon-box").removeClass("active-item");
			$("#ih6").addClass("active-item");
			$("#about-info-default, #about-info-3, #about-info-4, #about-info-5, #about-info-2").hide();
			$("#about-info-6").fadeIn(450).css({"display":"flex"});

		});

});


// PROCESS CLICK AND REVEAL
$(document).ready(function() {
    "use strict";
    //btn1
   $("#process-box-icon-1").click(function() {
       $("#process-box-icon-2, #process-box-icon-3, #process-box-icon-4").removeClass("active-box");
       $(this).addClass("active-box");
       $(".process-boxs").removeClass("active-item");
       $("#process-icon-1").addClass("active-item");
       $("#process-box-info-2, #process-box-info-3, #process-box-info-4").hide();
       $("#process-box-info-1").fadeIn(450).css({"display":"flex"});
   });

   //btn2
    $("#process-box-icon-2").click(function() {
        $("#process-box-icon-1, #process-box-icon-3, #process-box-icon4").removeClass("active-box");
        $(this).addClass("active-box");
        $(".process-boxs").removeClass("active-item");
        $("#procees-icon-2").addClass("active-item");
        $("#process-box-info-1, #process-box-info-3, #process-box-info-4").hide();
        $("#process-box-info-2").fadeIn(450).css({"display":"flex"});
    });

    //btn3
    $("#process-box-icon-3").click(function() {
        $("#process-box-icon-1, #process-box-icon-2, #process-box-icon-4").removeClass("active-box");
        $(this).addClass("active-box");
        $(".process-boxs").removeClass("active-item");
        $("#process-icon-3").addClass("active-item");
        $("#process-box-info-1, #process-box-info-2, #process-box-info-4").hide();
        $("#process-box-info-3").fadeIn(450).css({"display":"flex"});
    });

    //btn4
    $("#process-box-icon-4").click(function() {
        $("#process-box-icon-1, #process-box-icon-2, #process-box-icon-3").removeClass("active-box");
        $(this).addClass("active-box");
        $(".process-boxs").removeClass("active-item");
        $("#process-icon-4").addClass("active-item");
        $("#process-box-info-1, #process-box-info-2, #process-box-info-3").hide();
        $("#process-box-info-4").fadeIn(450).css({"display":"flex"});
    });

});

