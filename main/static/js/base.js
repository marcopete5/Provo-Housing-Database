// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
$(document).ready(function(){
	$('#listview').hide();
	$('.list').click(function(){
		$('#map').hide();
		$('#listview').fadeIn('fast');
	});

	$('.map').click(function(){
		$('#map').show();
		$('#listview').fadeOut('fast');
	});

	$('.list').hover(function(){
		$
	});

	$('.complex').click(function(){
		$(this).next().fadeIn('fast');
	})

	$('#div_id_address').hide();
	$('#div_id_city').hide();
	$('#div_id_state').hide();
	$('#div_id_apartment_complex').click(function(){
		$('#div_id_address').toggle(this.checked);
		$('#div_id_city').toggle(this.checked);
		$('#div_id_state').toggle(this.checked);
		$('#div_id_complex_name').toggle(this.checked);
	}) 
})

	


 $('#id_upload_image').change(function(){
            if ($(this).files && $(this).files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#id_upload_image')
                        .attr('src', e.target.result)
                        .width(150)
                        .height(200);
                };

                reader.readAsDataURL($(this).files[0]);
            }
        })
$("#search").keyup(function () {
	var searchTerm = $("#search").val();
	var addresses = $("#listings").find(".address");

	$.extend($.expr[':'], {
		'containsi': function (elem, i, match, array) {
			return (elem.textContent || elem.innerText || '').toLowerCase()
				.indexOf((match[3] || "").toLowerCase()) >= 0;
		}
	});

	var searchSplit = searchTerm.replace(/ /g, "'):containsi('");

	$("#listings .address").not(":containsi('" + searchSplit + "')").each(function (e) {
		$(this).parent().parent().addClass('hidden');
		
//			console.log($(this).parent());
	});

	$("#listings .address:containsi('" + searchSplit + "')").each(function (e) {
		$(this).parent().parent().removeClass('hidden');
	});

});

function filter_data(data) {
	return data 

}


function withDelay(data, x, map, myVar)
{
	console.log('dl:'+data.length)
	if (x == data.length)
	{
		clearInterval(myVar)
	}
	else
	{
		console.log('x is: '+x)
		geocoder = new google.maps.Geocoder();
		// console.log('data:'+data[x].fields.address)
		// console.log("x= "+x)
		
		// codeAddress(data, x, geocoder, map)
		x++
	}

	
			

}


function initMap() 
{
	var map = new google.maps.Map(document.getElementById('map'), 
	{

			center: {lat: 40.2573138, lng: -111.7089457},
		 
			zoom: 13,
			mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	 // Create the search box and link it to the UI element.
	var input = document.getElementById('pac-input');
	var searchBox = new google.maps.places.SearchBox(input);
	map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

	// Bias the SearchBox results towards current map's viewport.
	map.addListener('bounds_changed', function() 
	{
		searchBox.setBounds(map.getBounds());
	});

	var geocoder = new google.maps.Geocoder();
	$.get("http://127.0.0.1:8000/housing_api", function(data, status)
	{
		data = filter_data(data)
		// console.log(data)
		console.log('________ data _____________'+data)


		var x = 1;
		// var myVar = setInterval(withDelay, 1000);
	});//close get housing_api
}


		function codeAddress(data, x, geocoder, map) 
		{
			console.log('entering codeAddress function')
			var markerOptions = 
			{
				map
			}

			if (data[x].model == 'main.complexname') 
			{
				var address =  data[x].fields.address +' USA'
				var complex_name = data[x].fields.name
				console.log(x+' complex address: '+address+' Name: '+complex_name)
			} 
			else 
			{
				var address = data[x].fields.address+' '+data[x].fields.city+', '+data[x].fields.state
				console.log(x+' apartment address: '+address+' Name: '+complex_name)
			}
			
			location.LatLng
			geocoder.geocode( { 'address': address }, function(results, status) 
			{

				console.log('geocode results: '+results+' And status: '+status)
				latitude = results[0].geometry.location.lat() 
				longitude = results[0].geometry.location.lng()

				console.log("x= "+x)


				if (status == 'OK') 
				{
					console.log('status from google is:'+status)
					console.log("data[x].model: "+data[x].model)
					if (data[x].model == 'main.complexname') 
					{

						var myLatlng = new google.maps.LatLng(data[x].fields.latitude, data[x].fields.longitude);
						map.setCenter(results[0].geometry.location);
						console.log('a complex:')
						var marker = new google.maps.Marker
						({

								map: map, 
								position: myLatlng,
								url: 'http://127.0.0.1:8000/single_complex/'+data[x].pk,
								title:data[x].fields.name

						}); //var marker
						console.log('-----'+myLatlng+'-----')
						google.maps.event.addListener(marker, 'click', function() 
						{
							window.location.href = marker.url;
						});
						console.log("big red marker complex: "+x)

					} 
					else if (data[x].model == 'main.listing') 
					{
						map.setCenter(results[0].geometry.location);
						var marker = new google.maps.Marker
						({
								icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
								map: map, 
								position: results[0].geometry.location,
								url: 'http://127.0.0.1:8000/listing/'+data[x].pk,
						}); //var marker
						console.log("blue marker elif: "+x)
						google.maps.event.addListener(marker, 'click', function() 
						{
							window.location.href = marker.url;
						});
					} 
				} 
				else     // ====== Decode the error status ======
				{
					console.log('else not OK')
					// === if we were sending the requests too fast, try this one again and increase the delay
					if (status == 'OVER_QUERY_LIMIT') 
					{
						console.log('OVER_QUERY_LIMIT')
						nextAddress--;
						delay++;
					} 
					else 
					{
						var reason="Code "+status;
						var msg = 'address="' + search + '" error=' +reason+ '(delay='+delay+'ms)<br>';
						document.getElementById("messages").innerHTML += msg;
					}   

					console.log('^^^^^^^^^^^^^^^^')
				}

			}); //geocoder.geocode
		};




