<!DOCTYPE html>
<html>
<head>
	<title>MySQL from PHP</title>
		<link rel="stylesheet" href="css/base.css" />
</head>
<body>
<pre><?php print_r($_POST); ?></pre>
	<h1>Student demo</h1>
<?php
	/* Use your own database information */
	$dbc= @mysqli_connect("localhost", "bowditcw", "H8zFAA2E", "bowditcw") or
					die("Connect failed3: ". mysqli_connect_error());
					
	
	
	
	//$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
	$position = $_POST['position'];
	if ( $_POST['name'] != null ) {
		$name = $_POST['name'];
		
		if ( $_POST['email'] != null ) {
			$email = $_POST['email'];
			
			$email_query = "select email from club where email = '$email'";
			$result = mysqli_query($dbc, $email_query) or die("bad query".mysqli_error($dbc));	
			$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
			$email1 = $row['email'];
			if( $email1 == null ) {
				if ( $_POST['password'] != null) {
					$password = $_POST['password'];
					
					if ( $_POST['password2'] != null) {
						$password2 = $_POST['password2'];
						
						if ($password == $password2) {
							handleform($dbc,$name,$email,sha1($password),$position);
						}
						else echo "Passwords don't match";
					}
					else echo 'No Password2 Entered';
					
				}
				else echo 'No Password Entered';
			}
			else echo 'Email Already Exists';
		}
		else echo 'No Email Entered';
	}
	else echo 'No Name Entered';
	echo "<br><br>";
	echo "<a href='http://cscilab.bc.edu/~bowditcw/club'>Back to Home Page</a>";
?>

</body>
</html>
<?php
function performQuery($dbc, $query){
	$result = mysqli_query($dbc, $query) or die("bad query".mysqli_error($dbc));
	return $result;
}


function handleform($dbc,$name,$email,$password,$position){
	$query = "INSERT INTO club VALUES ('$name', '$email', '$password',now(),'$position')";
	$result = performQuery($dbc, $query);
	if ( ! $result )
		echo "<br>Oops! Something went wrong";
	else
		echo "<br>Congratulations on joining the Crew Team!";
	echo "<a href='http://cscilab.bc.edu/~bowditcw/club'>Back to Home Page</a>";
	//mysqli_query($dbc, $insert_query);
	//echo "Insertion Complete";

}
?>