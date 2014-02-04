
$(document).ready(function(){
    //Google Maps
    //Default starting point
    var latlng = new google.maps.LatLng(40.737897, -111.859462);
    var mapOptions = {
        zoom: 1,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    //Create our map
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    //Find address
    var address = $("#address").text();
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address }, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            map.setZoom(10);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location,
                url: 'http://maps.google.com/?q=' + $("#address").text()
            });
            google.maps.event.addListener(marker, 'click', function() {
                window.open(marker.url, "_blank");
            });
        }
        else {
            $("#map-message").removeClass("hidden");
        }
    });
});