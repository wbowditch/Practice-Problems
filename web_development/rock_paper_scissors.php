<!DOCTYPE html>

<html lang="en">
<head>
     <meta charset="utf-8" />
     <title>Bowditch: HW4</title>
     <style>
     	body {background-color: gray}
     	h1 {color: green}
     	h4 {color: purple}
     	</style>
</head>
<body>
<center><h1> Let's Play!</h1><center>
<br>
<h4> Rock Paper Scissors </h4>
<br>

<form method = "get" action="rps_compute.php" id="elementform">
<input type="radio" form = "elementform" name="element" value="Rock" checked>Rock
<br>
<input type="radio" name="element" form = "elementform" value="Paper" checked>Paper
<br>
<input type="radio" name="element" form = "elementform" value="Scissors" checked>Scissors
<br>
<img src="rps.jpg" alt="RPS" />
<br>
<input type="submit">
</form>
</body>


</html>
