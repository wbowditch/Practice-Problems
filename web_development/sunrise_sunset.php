<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>Bowditch: HW5</title>
	<meta name="generator" content="BBEdit 11.0" />
	<style>
		td {
			border-right: 1px solid #C1DAD7;
			border-bottom: 1px solid #C1DAD7;
			background: #fff;
			padding: 6px 6px 6px 12px;
			color: #6D929B;
		}
		table{
			border-left: 1px solid #C1DAD7;
		}
		th {
			font: bold 11px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
			color: "tan";
			border-right: 1px  solid #C1DAD7;
			border-bottom: 1px solid #C1DAD7;
			border-top: 1px solid #C1DAD7;
			letter-spacing: 2px;
			text-transform: uppercase;
			text-align: left;
			padding: 6px 6px 6px 12px;
			background: #CAE8EA ;
		}
		body {  background-color: tan; 
				font: bold 11px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
		}
		legend {
			font: bold 16px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
		}
		input {
			font: bold 16px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
			background: #fff;
		}
	</style>
</head>
<body>
<h1>Sunrise and Sunset</h1>
<?php

	$longitude = 0;
	$latitude = 0;
	$gmt_offset = 0;
	$now = time();

	displayform();

	if ( isset( $_GET['city'] ) ) {
		//echo $_GET['submitted'];
		handleform();
	}
	else{
	echo "<h1>Choose a City</h1>";
	}
?>

</body>
</html>
<?php
function displayform(){
?>
<fieldset>
	<legend>Select a City</legend>
	<form method="get">
		<br><br>
		
		Los Angeles: <input type="radio" name="city" value="Los Angeles"/>
		Boston: <input type="radio" name="city" value="Boston"/>
		Edinburgh: <input type="radio" name="city" value="Edinburgh"/>
		<br><br><br><br><br><br>
		
		<input type="submit" name="submitted" value="Get Sunrise and Sunset Data"/>
				
</form>
</fieldset>
<?php
}

	
//$city = $_GET['city'];


function create_sunrise_sunset_table( $city ){




if ($city == "Boston"){
	//echo "<h1>boston</h1>";
	$longitude = -71.05690;
	$latitude = 42.35670;
	$gmt_offset = 5;
	}
else if($city == "Los Angeles" ){

	$longitude = -118.24100;
	$latitude = 35.05420;
	$gmt_offset = 8;
	}
else if ($city == "Edinburgh"){

	$longitude = -3.16670;
	$latitude = 55.95000;
	$gmt_offset = 0;
	
}
else{
	$city = null;
	exit("<h1>Error: Nothing Chosen</h1>");

}
$now = time();	// get the current date and time
	
	// turn off php and write the table header in html
	?>	
	
	<fieldset>
	<legend>Results Table</legend>
	<table>
		<tr>
			<th>SUNRISE</th>
			<th>SUNSET</th>
			<th>DATE</th>
		</tr>
	<?php
	
	// do this for the next 7 days
	// each time through the loop, I make one row of the table.
	for ( $i = 0; $i < 7; $i++ ) {
		$sunrise_time = date_sunrise( $now, SUNFUNCS_RET_STRING, $latitude, $longitude, 90, $gmt_offset );
		$sunset_time = date_sunset( $now, SUNFUNCS_RET_STRING, $latitude, $longitude, 90, $gmt_offset );
		$formatted_date = date( "D M d Y", $now );

		echo "<tr>
					<td>$sunrise_time</td><td>$sunset_time</td><td>$formatted_date</td>
			  </tr>\n";

		$now += 24 * 60 * 60;  // add a days worth of seconds to $now
	}
	// turn off php and close the table tag.
?>
	</table>
	</fieldset>
	<?php





}

	
function handleform() {
	// This is to get rid of an annoying warning message...
	date_default_timezone_set(@date_default_timezone_get());
	//if($city!=null){
	//global $city;
	create_sunrise_sunset_table($_GET['city'] );
	//}
	//echo $_GET['city'];
	//global $latitude, $longitude, $gmt_offset;
	//echo $_GET['latitude'];



	
}
