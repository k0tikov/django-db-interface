 var arr_first = new Array("2013");
 var arr_last = new Array("2025")
 var arr_2013 = new Array("2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025");
 var arr_2014 = new Array("2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025");
 var arr_2015 = new Array("2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025");
 var arr_2016 = new Array("2016","2017","2018","2019","2020","2021","2022","2023","2024","2025");
 var arr_2017 = new Array("2017","2018","2019","2020","2021","2022","2023","2024","2025");
 var arr_2018 = new Array("2018","2019","2020","2021","2022","2023","2024","2025");
 var arr_2019 = new Array("2019","2020","2021","2022","2023","2024","2025");
 var arr_2019 = new Array("2019","2020","2021","2022","2023","2024","2025");
 var arr_2020 = new Array("2020","2021","2022","2023","2024","2025");
 var arr_2021 = new Array("2021","2022","2023","2024","2025");
 var arr_2022 = new Array("2022","2023","2024","2025");
 var arr_2023 = new Array("2023","2024","2025");
 var arr_2024 = new Array("2024","2025");
 var arr_2025 = new Array("2025");
 var len;

 function Add_option_to_select()
 {
	var CountryObj = document.getElementById("id_start_year");
	var ResortObj = document.getElementById("id_end_year");
	var selind = CountryObj.options.selectedIndex;

	switch (selind)
	{
	  case 0:
	    ResortObj.options.length = 1; 
		ResortObj[0] = new Option("", arr_2025[0]);
	    break;

	  case 1:
	    ResortObj.options.length = 0;
		len= arr_2013.length;
	   // alert(len);
	    for (var n = 0; n < len; n++)
	    {
			ResortObj[n] = new Option(arr_2013[n], arr_2013[n]);
	    }
	    break;
		
	  case 2:
	    ResortObj.options.length = 0;
	    len= arr_2014.length;
	    for (var n = 0; n < len; n++)
	    {
			ResortObj[n] = new Option(arr_2014[n], arr_2014[n]);
	    }
	    break;
		
	  case 3:
		ResortObj.options.length = 0;
		len= arr_2015.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2015[n], arr_2015[n]);
	    }
	    break;
		
	  case 4:
		ResortObj.options.length = 0;
		len= arr_2016.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2016[n], arr_2016[n]);
	    }
	    break;
		
	  case 5:
		ResortObj.options.length = 0;
		len= arr_2017.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2017[n], arr_2017[n]);
	    }
	    break;
	  
	  case 6:
		ResortObj.options.length = 0;
		len= arr_2018.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2018[n], arr_2018[n]);
	    }
	    break;
		
	  case 7:
		ResortObj.options.length = 0;
		len= arr_2019.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2019[n], arr_2019[n]);
	    }
	    break;
		
	  case 8:
		ResortObj.options.length = 0;
		len= arr_2020.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2020[n], arr_2020[n]);
	    }
	    break;
	
	  case 9:
		ResortObj.options.length = 0;
		len= arr_2021.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2021[n], arr_2021[n]);
	    }
	    break;
	
	  case 10:
		ResortObj.options.length = 0;
		len= arr_2022.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2022[n], arr_2022[n]);
	    }
	    break;
		
      case 11:
		ResortObj.options.length = 0;
		len= arr_2023.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2023[n], arr_2023[n]);
	    }
	    break;
		
	  case 12:
		ResortObj.options.length = 0;
		len= arr_2024.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2024[n], arr_2024[n]);
	    }
	    break;
	
	  case 13:
		ResortObj.options.length = 0;
		len= arr_2025.length;
	    for (var n = 0; n < len; n++)
	    {
	       ResortObj[n] = new Option(arr_2025[n], arr_2025[n]);
	    }
	    break;
	}
 }