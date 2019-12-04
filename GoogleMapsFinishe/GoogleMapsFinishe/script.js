function initMap(){
    var myPerson = {lat : 77.5011, lng: 27.2018};
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom:4, center: myPerson});

    var marker = new google.maps.Marker({position:myPerson , map:map});
}