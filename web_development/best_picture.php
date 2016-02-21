<!DOCTYPE html>
<html lang="en">
<head>
<style>
	body {background-color:lightgray}
	h1 {color:yellow}
	h1 {background-color:black}
	img {float: right}
	</style>
	<meta charset="utf-8" />
	<title>2015 Best Picture</title>
</head>
<h1> 2015 Best Picture</h1>
<br>
<h3>...And the Oscar goes to...</h3>
Have you seen the movies in the list below?
<input type="radio" name="seen" value="yes" checked>Yes
<input type="radio" name="seen" value="no" checked>No
<br><br>
<body>

<form name="htmlform" method="post" action="http://cscilab.bc.edu/~turinga/hw2/hw2action.php">
<select name="winner" size="8" multiple="multiple">
<option value="American Sniper">American Sniper</option>
<option value="The Imitation Game">The Imitation Game</option>
<option value="Selma">Selma</option>
<option value="Birdman or(The Unexpected Virtue of Ignorance)">Birdman or(The Unexpected Virtue of Ignorance)</option>
<option value="Boyhood">Boyhood</option>
<option value="The Theory of Everything">The Theory of Everything</option>
<option value="The Grand Budapest Hotel">The Grand Budapest Hotel</option>
<option value="Whiplash">Whiplash</option>
</select>
<table width="450px">
</tr>

<tr>

<img src = "Oscars.jpg" alt=  "Oscars" height = "380" width = "600">
 
<br><br>
 <td valign="top">
  <label for="name">Please enter your name: </label>
 </td>
 <td valign="top">
  <input  type="text" name="name" maxlength="50" size="30">
 </td>
</tr>
 
<tr>
 <td valign="top"">
  <label for="address">Please enter your address: </label>
 </td>
 <td valign="top">
  <input  type="text" name="address" maxlength="50" size="30">
 </td>
</tr>
<tr>
 <td valign="top">
  <label for="email">Please enter your email: </label>
 </td>
 <td valign="top">
  <input  type="text" name="email" maxlength="80" size="30">
 </td>
 
</tr>
<input type="checkbox" name="send" value="Yes"> Send me the results<br>
<tr>
 
</tr>
<tr>
 <td colspan="2" style="text-align:center">
  <input type="submit" value="Record My Vote">   <input type="reset" value="Reset!">
  <input type="hidden" name= "Recipient" value="Academy" >
  <input type="hidden" name= "Subject" value = "2015 Best Picture" >
 </td>
</tr>
</table>
</form>
<br><br><br>
Image Source: http://www.awardscircuit.com/wp-content/uploads/2014/02/Oscars.jpg
</body>
</html>