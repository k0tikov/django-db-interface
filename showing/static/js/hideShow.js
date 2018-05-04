$(window).on('load', function hideShow(){
	
	var hide_form = $('#content');
	/*var array_of_tags = [
					 document.getElementById('id_checkbox_input_0'),
					 document.getElementById('id_checkbox_input_1'),
					 document.getElementById('id_checkbox_input_2'),
					 document.getElementById('id_checkbox_input_3'),
					 document.getElementById('id_checkbox_input_4'),
					 document.getElementById('id_checkbox_input_5'),
					 document.getElementById('id_checkbox_input_6'),
					 document.getElementById('id_checkbox_input_7')			 
					 ];*/
	var array_of_tags = [
					 $('#id_checkbox_input_0'),
					 $('#id_checkbox_input_1'),
					 $('#id_checkbox_input_2'),
					 $('#id_checkbox_input_3'),
					 $('#id_checkbox_input_4'),
					 $('#id_checkbox_input_5'),
					 $('#id_checkbox_input_6'),
					 $('#id_checkbox_input_7')			 
					 ];			 
	var count = 0;
	for (var i = 0; i <= array_of_tags.length; i++ ){
		if ($(array_of_tags[i]).prop("checked") == true){
		count ++;
		};
	};
	console.log(count)
	if (count > 0){
		$('#fieldset').hide();
		/*$('#excel-button').css('display', 'block');*/
		$('#excel-button').show();
	} else{
		$('#table-content-advanced').hide();
		$('#cross-asf').hide();
		
	};
	/*hide_form.css('display', 'block');*/
});