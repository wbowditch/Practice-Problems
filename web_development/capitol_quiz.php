<!DOCTYPE html>
<html>
<head>
  <title>BOWDITCH HW7: Capital Quiz</title>
  <style>
  	body {background-color: lightgreen; font-family: helvetica;}
  	input, legend {font-size: 150%;}
	select, option {font-size: 150%;}
	.mybutton {
		font-size: 150%;
		background-color: orange;
	}
	.mymenu {
		font-size: 150%;
		background-color: orange;
	}

  </style>
</head>
<body>
 <!-- Main body program, like static void main(String[] args) --!>
<?php # set up capitals array
$statecapital = array (
"Alabama" => "Montgomery",
"Alaska" => "Juneau",
"Arizona" => "Phoenix", 
"Arkansas" => "Little Rock", 
"California" => "Sacramento", 
"Colorado" => "Denver", 
"Connecticut" => "Hartford", 
"Delaware" => "Dover", 
"Florida" => "Tallahassee", 
"Georgia" => "Atlanta", 
"Hawaii" => "Honolulu", 
"Idaho" => "Boise",
"Illinois" => "Springfield", 
"Indiana" => "Indianapolis", 
"Iowa" => "Des Moines", 
"Kansas" => "Topeka", 
"Kentucky" => "Frankfort", 
"Louisiana" => "Baton Rouge", 
"Maine" => "Augusta", 
"Maryland" => "Annapolis", 
"Massachusetts" => "Boston", 
"Michigan" => "Lansing", 
"Minnesota" => "St. Paul", 
"Mississippi" => "Jackson", 
"Missouri" => "Jefferson City", 
"Montana" => "Helena",
"Nebraska" => "Lincoln", 
"Nevada" => "Carson City", 
"New Hampshire" => "Concord", 
"New Jersey" => "Trenton", 
"New Mexico" => "Santa Fe", 
"New York" => "Albany",
"North Carolina" => "Raleigh", 
"North Dakota" => "Bismarck", 
"Ohio" => "Columbus", 
"Oklahoma" => "Oklahoma City", 
"Oregon" => "Salem", 
"Pennsylvania" => "Harrisburg", 
"Rhode Island" => "Providence", 
"South Carolina" => "Columbia", 
"South Dakota" => "Pierre", 
"Tennessee" => "Nashville", 
"Texas" => "Austin",
"Utah" => "Salt Lake City", 
"Vermont" => "Montpelier", 
"Virginia" => "Richmond", 
"Washington" => "Olympia", 
"West Virginia" => "Charleston", 
"Wisconsin" => "Madison", 
"Wyoming" => "Cheyenne");
	if ( !isset( $_GET['total'] ) ) {   //if count hasn't been set yet
		$total = 0;						//set the total questions answered to 0
		$correct = 0;					//set the correct answers to 0
		}
		
	if ( isset( $_GET['capital'] ) ) {  //if a capital has been chosen       //get the state (defined in displayform)
		$iscorrect = check($statecapital, $_GET['state'],$_GET['capital']);  //boolean function that checks if state matches capital
		$total = $_GET['total']; 		//get the total questions answerd
		$correct = $_GET['correct'];    //get the total questions answered correctly
		if($statecapital[$_GET['state']] == $_GET['capital']){					//if answer is correct
			$correct++;					//increment the questions answered correctly
			}
		$total++;						//increment questions answered 
		handleform($iscorrect,$total,$correct,$statecapital);   //
	}
	displayform($statecapital,$total,$correct);

?>
<br>
</body>
</html>
<?php
function handleform($iscorrect,$total,$correct,$list){
	  $capital = $_GET['capital']; 						//get the capital chosen
      $state = $_GET['state'];							//get the state
      
      if ($iscorrect) {									
      	  echo "<fieldset>
      	  			<legend> YES!!!!</legend> <br>
          			<The capital of $state is
          			<h1> $list[$state]</h1>
          			<br>
          			You have $correct correct answers <br>
          			out of a total of $total questions
          		</fieldset>";
          		}
     else {
     	  echo "<fieldset>
      	  			<legend> WRONG! </legend> <br>
          			The capital of $state is 
          			<h1> $list[$state]</h1>
          			<br>
          			You have $correct correct answers <br>
          			out of a total of $total questions 
          		</fieldset>";
          		}

      
}

function displayform($list,$total,$correct){
	$state = array_rand($list, 1);
?>
	<fieldset><legend>The capital of <?php echo $state ?> is: </legend>
	<br><br>
<!-- Hidden sticky variables that need to be remembered by the form --!>
		<form method="get">
		<input type = "hidden" name = "total" value = "<?php echo $total ?>">
		<input type = "hidden" name = "state" value = "<?php echo $state ?>">  
		<input type = "hidden" name = "correct" value = "<?php echo $correct ?>">
			<?php make_state_pulldown($list, 'capital'); ?>
    		<input value = "Submit" name = "pressed" type = "submit">
		</form>
	</fieldset>
<?php
}

function check($list,$state,$capital) {
	if($list[$state] == $capital){ return true; }
	else {return false; }
	}


function make_state_pulldown($list, $name){
	echo "<select name=$name class='mymenu'>";
	asort($list);
	foreach($list as $key => $value) {
		if ( isset($_GET['capital']) ){
			if($value == $_GET['capital'])
			echo "<option selected= 'selected'>$value </option>";
			else{
				echo "<option>$value</option>";
				}
			}
		else {
			echo "<option>$value</option>";
			}
			}
	echo "</select>";
	
				
			
	
}
?>


