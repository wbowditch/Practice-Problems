<!DOCTYPE html>

<html lang="en">
<head>
     <meta charset="utf-8" />
     <title>HW1</title>
</head>
<body>
<? php 
	echo "print_r($_GET)";
	
	$bill = $_GET["total"];
	$percent = $_GET["tip"];
	$split = $_GET["split"];
	
	$tip = $bill*$percent;
	$total = $tip+$bill;
	$each = $total/$split;
	
	<h3> Results </h3>;
	echo "For the bill of $bill";
	<br>;
	echo "the tip is $tip";
	echo "for a total of $total";
	echo "and divided $split way(s)";
	echo "each person owes $each";
</html>