
// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
$(document).ready(function(){
	console.log('test')
	$('#listview').hide();

	$('.list').click(function(){
		$('#map').hide();
		$('#listview').fadeIn('fast');
		$('#pac-input').hide();
	});

	$('.map').click(function(){
		$('#map').show();
		$('#listview').fadeOut('fast');
		$('#pac-input').show();
	});

	$('.list').hover(function(){
		$
	});

	$('.complex').click(function(){
		console.log('test');
		$(this).next().fadeIn('fast');
	})
})
	




	function initMap() {
		var map = new google.maps.Map(document.getElementById('map'), {

			center: {lat: 40.2573138, lng: -111.7089457},
		 
			zoom: 12,
			mapTypeId: google.maps.MapTypeId.ROADMAP
	});
		var geocoder = new google.maps.Geocoder();
		$.get("http://127.0.0.1:8000/housing_api", function(data, status){
			var x;
			console.log(data)
			for (x = 0; x < data.length; x++) {
				

					geocoder = new google.maps.Geocoder();
					console.log('data:'+data[x].fields.address)
					function codeAddress() {
						var address = data[x].fields.address+' '+data[x].fields.city+', '+data[x].fields.state
						console.log('addy:'+address)
						// document.getElementById("address").value;
						console.log('geo  '+geocoder)
						geocoder.geocode( { 'address': address}, function(results, status) {
							if (status == google.maps.GeocoderStatus.OK) {
								//In this case it creates a marker, but you can get the lat and lng from the location.LatLng
								map.setCenter(results[0].geometry.location);
								var marker = new google.maps.Marker({
										map: map, 
										position: results[0].geometry.location
								});
							} else {
								alert("Geocode was not successful for the following reason: " + status);
							}
						});
					}
					codeAddress()
			}
		});//close get housing_api

	};




