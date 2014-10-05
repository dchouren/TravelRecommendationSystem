

function initialize() {

    // The photoDiv defines the DIV within the info window for
    // displaying the Panoramio photo within its PhotoWidget.
    var photoDiv =    document.createElement('div');

    // The PhotoWidget width and height are expressed as number values,
    // not string values.
    var photoWidgetOptions = {
        width: 640,
        height: 500
    };

    // We construct a PhotoWidget here with a blank (null) request as we
    // don't yet have a photo to populate it.
    var photoWidget = new panoramio.PhotoWidget(photoDiv, null,
            photoWidgetOptions);

    var monoLake = new google.maps.LatLng(37.973432, -119.093170);
    var mapCenter = new google.maps.LatLng(0,0); //Google map Coordinates
    var mapOptions = 
    { 
        center: monoLake, // map center
        zoom: 11, //zoom level, 0 = earth view to higher value
        panControl: true, //enable pan Control
        zoomControl: true, //enable zoom control
        zoomControlOptions: {
                style: google.maps.ZoomControlStyle.SMALL //zoom control size
        },
        scaleControl: true, // enable scale control
        mapTypeId: google.maps.MapTypeId.HYBRID // google map type
    };


    var recMaps = document.getElementsByClassName('map-canvas');
    for (int i = 0; i < recMaps.size(); i++) {
        var map = new google.maps.Map(document.getElementsByClassName('map-canvas'),
                    mapOptions);
    }
    

    var infoWindow = new google.maps.InfoWindow();
    var panoramioLayer = new google.maps.panoramio.PanoramioLayer({
        suppressInfoWindows: true
    });

    panoramioLayer.setMap(map);

    google.maps.event.addListener(panoramioLayer, 'click', function(e) {
        var photoRequestOptions = {
            ids: [{
                'photoId': e.featureDetails.photoId,
                'userId': e.featureDetails.userId
            }]
        };
        photoWidget.setRequest(photoRequestOptions);
        photoWidget.setPosition(0);
        infoWindow.setPosition(e.latLng);
        infoWindow.open(map);
        infoWindow.setContent(photoDiv);
    });

}

google.maps.event.addDomListener(window, 'load', initialize);

