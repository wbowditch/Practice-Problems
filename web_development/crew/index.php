<!DOCTYPE html>
<html>
<head>
  <title>Boston College Crew</title>
  <link rel = "stylesheet" href = "css/club.css"/>
</head>
<body>

<?php 
if ( !isset( $_GET['join_button'] ) ) { 
	display_form();
		}
else{
	display_form2();
	}
?>
</body>
</html>
<?php

function display_form(){
?>
	<fieldset><legend><h1>Boston College Crew Team</h1></legend>
	<br><br>
		<form method="get">
			<img src = "img/logo.png" alt=  "Logo">
    		<input type = "submit" id = "mybutton" name = "join_button" value = "Join Now">
		</form>
	</fieldset>
<?php
}

function display_form2(){
?>
	<fieldset><legend><h4>Fill Out Your Information Here</h4></legend>
	<br><br>
		<form method="post" action = "include/dboperations.php">
			<label for="name">Please enter your name: </label>
			<input type = "text" name = "name">
			<br><br>
			<label for="email">Please enter your email: </label>
			<input type = "text" name = "email">
			<br><br>
			<label for="password">Please enter your password: </label>
			<input type = "password" name = "password">
			<br><br>
			<label for="password2">Please confirm your password: </label>
			<input type = "password" name = "password2">
			<br><br>
			<input type="radio" name="position" value="Starboard" checked>Starboard
			<input type="radio" name="position" value="Port" checked>Port
			<input type="radio" name="position" value="Coxswain" checked>Coxswain
			<br><br>
    		<input type = "submit"  name = "submit_button" value = "Submit">
		</form>
	</fieldset>
<?php
}



				
			
	
?>


