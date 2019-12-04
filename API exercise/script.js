function loadDate() {
    var currentData = new Date();
    var dateString = currentData.toString().split("").join("");
    document.getElementById("date").innerHTML = dateString;
}


function loadWeather() {
    var url = "https://api.forecast.io/forecast/";
    var apiKey = "8097e7dbed16085188071f8873d82929";

    function success(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        $.getJSON(url + apiKey + "/" + latitude + "," + longitude + "?callback=?", function(data) {
            console.log(data);
           document.getElementById("weather").innerHTML = "Based on where you are, the temperature is " + data.currently.temperature + " degrees F right now";
        });

    }

    function error() {
        alert("it didn't work u messed up");
    }

    navigator.geolocation.getCurrentPosition(success, error);
}

function onLoad() {
    loadDate();
    loadWeather();
}

