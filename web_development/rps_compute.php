<!DOCTYPE html>

<html lang="en">
<head>
     <meta charset="utf-8" />
     <title>Bowditch: HW4</title>
     <style>
     body {background-color: tan}
     h4 {color: red}
     h3 {color: yellow}
     h2 {color: green}
     </style>
     </head>
<body>
<?php 
	//print_r($_GET);
	echo  "<h1>Results</h1>";
	echo "<br>";
	$element = $_GET["element"];
	echo "The user chose <b>$element</b>";
	echo "<br>";
	$computernum = rand(1,3);
	if($computernum==1) {
		$computermove = "Rock"; }
	if($computernum==2) {
		$computermove = "Paper"; }
	if($computernum==3) {
		$computermove = "Scissors"; }
	echo "The computer chose <b>$computermove</b>";
	echo "<br>";
	if($computermove=="Rock") {
		if($element=="Rock") {
			echo "<h3>Draw</h3>"; 
			echo "<br>";
			?>
			<img src="rock_draw.png" alt="Rock Draw" />
			<?php
			}
		if($element=="Paper") {
			echo "<h2>User Wins</h2>"; 
			echo "<br>";
			?>
			<img src="paper_rock.png" alt="Paper Rock" />
			<?php
			}
		if($element=="Scissors") {
			echo "<h4>Computer Wins</h4>";
			echo "<br>"; 
			?>
			<img src="rock_scissors.jpg" alt="Scissors Rock" />
			<?php
			}
			}
	if($computermove=="Paper") {
		if($element=="Paper") {
			echo "<h3>Draw</h3>";
			echo "<br>"; 
			?>
			<img src="paper_draw.jpeg" alt="Paper Draw" />
			<?php
			}
		if($element=="Scissors") {
			echo "<h2>User Wins</h2>";
			echo "<br>"; 
			?>
			<img src="scissors_paper.jpg" alt="Scissors and Paper" />
			<?php
			}
		if($element=="Rock") {
			echo "<h4>Computer Wins</h4>"; 
			echo "<br>";
			?>
			<img src="paper_rock.png" alt="Paper and Rock" />
			<?php
			}
			}
	if($computermove=="Scissors") {
		if($element=="Scissors") {
			echo "<h3>Draw</h3>"; 
			echo "<br>";
			?>
			<img src="scissors_draw.jpg" alt="Scissors Draw" />
			<?php
			}
		if($element=="Rock") {
			echo "<h2>User Wins</h2>"; 
			echo "<br>";
			
			?>
			<img src="rock_scissors.jpg" alt="Rock  and Scissors" />
			<?php
			}
		if($element=="Paper") {
			echo "<h4>Computer Wins</h4>";
			echo "<br>"; 
			?>
			<img src="scissors_paper.jpg" alt="Scissors and paper" />
			<?php
			}
			}
	echo "<br>";
	echo '<a href="http://cscilab.bc.edu/~bowditcw/hw4/hw4.php">Play Again </a>'
	?>
</body>
</html>