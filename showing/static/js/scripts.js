
/*  
$(document).ready(function() {
  $("[data-toggle]").click(function() {
    var toggle_el = $(this).data("toggle");
    $(toggle_el).toggleClass("open-sidebar");
  });
     
});
 
$(".swipe-area").(swipe(){
    swipeStatus:function(event, phase, direction, distance, duration, fingers)
        {
            if (phase=="move" && direction =="right") {
                 $(".container-mainpage").addClass("open-sidebar");
                 return false;
            }
            if (phase=="move" && direction =="left") {
                 $(".container-mainpage").removeClass("open-sidebar");
                 return false;
            }
        }
});

 */ 
$(window).on('load', function () {
    $("[data-toggle]").click(function () {
        var toggle_el = $(this).data("toggle");
        $(toggle_el).toggleClass("open-sidebar");
    });
});