function checkForm(form){
	
	/*var array_of_tags = [
					 document.getElementById('soft'),
					 document.getElementById('pnr'),
					 document.getElementById('shd'),
					 document.getElementById('server'),
					 document.getElementById('network'),
					 document.getElementById('support'),
					 document.getElementById('ibp'),
					 document.getElementById('consulting')
					 ];*/
	var array_of_tags = [
					 document.getElementById('id_checkbox_input_0'),
					 document.getElementById('id_checkbox_input_1'),
					 document.getElementById('id_checkbox_input_2'),
					 document.getElementById('id_checkbox_input_3'),
					 document.getElementById('id_checkbox_input_4'),
					 document.getElementById('id_checkbox_input_5'),
					 document.getElementById('id_checkbox_input_6'),
					 document.getElementById('id_checkbox_input_7')			 
					 ];	 
	var error_mes = document.getElementById('form-error');
	var text_input = document.getElementById('typeahead');
	var count = 0;
	for (var i = 0; i <= array_of_tags.length; i++ ){
		if ($(array_of_tags[i]).prop("checked") == true){
		count ++;
		};
	};
	/*if ((text_input.value != '') & (count > 0)){
		return true;
	};*/
	if (count > 0){
		return true;
	};
	error_mes.style.display = 'inline'
	
    return false;
	};
