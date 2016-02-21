<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>checkbox example</title>
	  <style>
			body {background-color: lightblue; font-family: helvetica;}
			input, legend {font-size: 150%;}
			select, option {font-size: 400%;}
			.mybutton {
				font-size: 250%;
			}
			.mycb {
				font-size: 250%;
			}
  </style>

</head>
<body>
<?php $mycolors = array("mushrooms", "peppers", "onions", "tomatoes", "spinach");
	$mymeat = array("pepperoni", "sausage", "bbq chicken", "proscutto", "ham");
	$mysize = array("small", "medium", "large");
	$mycrust = array("white", "whole wheat", "stuffed");
	if ( isset( $_GET['mycolors_'] ) ) {
		handleform($_GET['mycolors_']);
	}
	displayform($mycolors,$mymeat,$mysize,$mycrust);

?>
<br>
</body>
</html>
<?php
function handleform($chosencolors){
	  echo "<fieldset>
				<legend>The chosen colors are: </legend>";
	  $colors = implode($chosencolors, ", ");
	  echo "I chose $colors<br><br>";
	  
	  foreach ($chosencolors as $c) {
		echo "I chose $c <br>";
	  }
	  
	  echo "</fieldset>"; 
}

function displayform($list1,$list2,$list3,$list4){
?>
	<fieldset><legend>Toppings</legend>
		<form method="get">
			<?php createcheckboxes($list1, "mycolors"); ?>
	</fieldset>
	<fieldset><legend>Meat</legend>
			<?php createcheckboxes($list2, "mymeat"); ?>
    		
	</fieldset>
	<fieldset><legend>Size</legend>
			<?php createcheckboxes($list3, "mysize"); ?>
	</fieldset>
	<fieldset><legend>Crust</legend>
			<?php createcheckboxes($list4, "mycrust"); ?>
	</fieldset>
	<input class="mybutton" value="Choose em" type="submit">
	</form>
<?php
}

function createcheckboxes($list, $list2,$list3,$list4,$name){
	echo "<div class='mycb'>";
	foreach($list as $listitem) {
		echo "<input type='checkbox' name='$name []' value='$listitem'> $listitem <br>\n";
	}
	echo "</div>";

}
