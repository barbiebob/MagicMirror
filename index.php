<!doctype html>
<html lang="sv">
<head>
	<meta charset="utf-8">
	<title>Magic Mirror</title>
  <meta name="description" content="The Magic Mirror">
	<!--<meta http-equiv="refresh" content="600" charset="utf-8">--> <!-- Updates the whole page every 10 minutes (each 600 second) -->
	<link rel="stylesheet" href="style.css">
	<link href='http://fonts.googleapis.com/css?family=Roboto:300' rel='stylesheet' type='text/css'>
		<script language="JavaScript"> <!-- Getting the current date and time and updates them every second -->
			setInterval(function() { 
				var currentTime = new Date ( );
				var currentHours = currentTime.getHours ( );
				var currentMinutes = currentTime.getMinutes ( );
				var currentMinutesleadingzero = currentMinutes > 9 ? currentMinutes : '0' + currentMinutes;
				var currentDate = currentTime.getDate ( );
	
					var weekday = new Array(7);
					weekday[0] = "Söndag";
					weekday[1] = "Måndag";
					weekday[2] = "Tisdag";
					weekday[3] = "Onsdag";
					weekday[4] = "Torsdag";
					weekday[5] = "Fredag";
					weekday[6] = "Lördag";
				var currentDay = weekday[currentTime.getDay()]; 
	
					var actualmonth = new Array(12);
					actualmonth[0] = "Januari";
					actualmonth[1] = "Februari";
					actualmonth[2] = "Mars";
					actualmonth[3] = "April";
					actualmonth[4] = "Maj";
					actualmonth[5] = "Juni";
					actualmonth[6] = "Juli";
					actualmonth[7] = "Augusti";
					actualmonth[8] = "September";
					actualmonth[9] = "Oktober";
					actualmonth[10] = "November";
					actualmonth[11] = "December";
				var currentMonth = actualmonth[currentTime.getMonth ()];

    var currentTimeString = "<h1>" + currentHours + ":" + currentMinutesleadingzero + "</h1><h2>" + currentDay + " " + currentDate + " " + currentMonth + "</h2>";
    document.getElementById("clock").innerHTML = currentTimeString;
}, 1000);
	</script>
</head>
<body>
<div id="wrapper">
  <!-- Clock -->
  <div id="upper-left">
    <div id="clock"></div>
  </div>
  <!-- Weather -->
  <div id="upper-right">
    <h2>
    <script src="jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(function() {
      getWeather();
    });
    function getWeather() {
      $('div#upper-right').load("./scripts/weather.py");
      setTimeout("getWeather()",600000);
    }
    </script>
    </h2>
  </div>
  <!-- Train departures -->
  <div id="middle-left">
    <p class="bigger">Avgångar Vikingstad</p><br />
    <script src="jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(function() {
      getTrains();
    });
    function getTrains() {
      $('div#middle-left').load("./scripts/trains.py");
      setTimeout("getTrains()",300000);
    }
    </script> 
  </div>
  <!-- DN news feed -->
  <div id="middle-right">
    <script src="jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(function() {
      getNews();
    });
    function getNews() {
      $('div#middle-right').load("./scripts/news.php");
      setTimeout("getNews()",60000);
    }
    </script>
  </div>
  <!-- Sonos viewer -->
  <img src="img/sonos.gif" class="displayed" alt="Sonos img" style="width:200px;height:38px;"> <br /> <br /> <br />
  <div id="bottom">
    <script src="jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">
    $(function() {
      getSonos();
    });
    function getSonos() {
      $('div#bottom').load("./scripts/sonos.py");
      setTimeout("getSonos()",2000);
    }
    </script>
  </div>
</div>
</body>
</html>
