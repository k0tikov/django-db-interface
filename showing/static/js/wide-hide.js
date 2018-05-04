$(window).on('load', function () {
    $('.button-cross').click(function(){
		var fields = $('.gl-td8, .gl-td9, .gl-td10, .gl-td11, .gl-td12, .gl-td13, .gl-td14')
		var titles = $('#gl-th8, #gl-th9, #gl-th10, #gl-th11, #gl-th12, #gl-th13, #gl-th14')
		/*if ($('.gl-td14').is(':hidden')){
			$('.gl-table').show();*/
		if ($(fields).is(':hidden')){
			$(fields).show();
			$(titles).show();
			$(this).addClass('descrease');
			
		}
		else{
			$(fields).hide();
			$(titles).hide();
			$(this).removeClass('descrease');
		}
    })
});