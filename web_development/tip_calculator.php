<!DOCTYPE html>

<html lang="en">
<head>
     <meta charset="utf-8" />
     <title>Bowditch: HW3</title>
     <style>
     	body {background-color: gray}
     	h1 {color: green}
     	h4 {color: purple}
     	</style>
</head>
<body>
<center><h1> Welcome to the Tip Calculator!</h1><center>
<br>
<h4> Tip Calculator </h4>
<br>
<form method = "get" action="firstcompute.php" id="tipform">
  Enter Amount: $<input type="text" name="total">
  <select name="tip" form="tipform">
  <option value=.1>Miserable</option>
  <option value=.12>Iffy</option>
  <option value=.15>Okay</option>
  <option value=.18>Good</option>
  <option value=.20>Really Great</option>
</select>
  <select name="split" form="tipform">
  <option value=1>No</option>
  <option value=2>Yes, two ways</option>
  <option value=3>Yes, three ways</option>
  <option value=4>Yes, four ways</option>
</select>
  <input type="submit">
</form>


</html>
