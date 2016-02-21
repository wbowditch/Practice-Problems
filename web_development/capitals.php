<html>
  <head>
    <title>Bowditch HW8</title>
    <style>
    .news {
    	overflow: auto;
    	height: 300px;
    	border: 3px groove blue;
	}
	</style>
  </head>
  <body>
  <?php # set up capitals array
  $news_source = array(
  	"http://feeds.reuters.com/reuters/businessNews"=>"Reuters",
  	"http://rss.nytimes.com/services/xml/rss/nyt/Space.xml"=>"NYTimes",
  	"http://rss.cnn.com/rss/cnn_world.rss"=>"CNN");
  	
  $weatherlocs = array(
    "http://w1.weather.gov/xml/current_obs/KBOS.xml"=>"Boston",
    "http://w1.weather.gov/xml/current_obs/KORD.xml"=>"Chicago",
    "http://w1.weather.gov/xml/current_obs/KROC.xml"=>"Rochester");
    
    //displayform($weatherlocs);
    //$place = $_GET['place'];
    //echo "$place";
    displayform($weatherlocs,$news_source);
    if (isset( $_GET['place'] )) {
    	//echo "$file";
    	//$file = $_GET['file'];
    	//$place = $_GET['place'];
    	    	//$place = $weatherlocs['place'];
    	//$file = $_GET['file'];
    	//$file = $_GET['file'];
    	//echo "$weatherlocs[$place]";
    	handleform($weatherlocs);
    	} 
    if (isset( $_GET['source'] )) {
    	handleform2($news_source);
    	}
    ?>


    <?php
 	?>

  </body>
</html>

<?php
function displayform($weatherlocs,$news_source){
	//$file = array_search($place, $weatherlocs);

	?>
	<fieldset><legend>My Weather</legend>
	<form method = "get">
	<?php create_menu($weatherlocs,'place'); 
	//echo "$file"; 
	?>
	<input type = "hidden" name = "file" value = "<?php echo $file ?>">
	<input type="submit" name="formsubmitted" value="Submit"/>
	</form>
	</fieldset>
	
	<fieldset><legend>My News</legend>
	<form method = "get">
	<?php create_menu($news_source,'source'); 
	?>
	<input type="submit" name="formsubmitted2" value="Submit"/>
	</form>
	</fieldset>
	

<?php }
function create_menu($list,$name) {
	echo "<select name=$name class='mymenu'>";
	asort($list);

	foreach($list as $key => $value) {
		echo "<option selected= 'selected'>$value </option>";
		}
	echo "</select>";
	}
function handleform($weatherlocs) {
	//echo "$weatherlocs"; // check the pull-down
	$place = $_GET['place'];
	$file = array_search($place, $weatherlocs);
          //$place = $weatherlocs[$file];
	//echo "$place is $file";
          //$file = $weatherlocs[$file];
          //echo "$weatherlocs[$place]";
          
    
	
	//$file = array_rand($weatherlocs, 1);
	if ( ! $xmlstr = file_get_contents( $file ) )
		die( "Unable to read XML file $file" );
	$xml = new SimpleXMLElement( $xmlstr );
	$location = $xml -> location;
	$obs = $xml -> observation_time;
	$tempf = $xml -> temp_f;
	$tempc = $xml -> temp_c;
	$wind = $xml -> wind_string;
	$weather = $xml -> weather;
	$icon = $xml -> icon_url_base;
	echo "<fieldset><legend> The Weather in $location</legend> <br>
			<h1>$obs</h1><br>
			<h3>$tempf F ($tempc C) $wind $weather <h3>
			</fieldset>";
	}
function handleform2($news_source) {
	//echo "$weatherlocs"; // check the pull-down
	$source = $_GET['source'];
	$file = array_search($source, $news_source);
	$rss= new SimpleXMLElement(file_get_contents($file));
    $title =  $rss->channel->title;
    echo "<h1>$title</h1>";



      $items = $rss->channel->item; # try, works some versions
      if (!$items)
        $items = $rss->item; # works other versions
	  //echo "$items";
	  $title = $items ->title;
	  $description = $items[0]->description;
	  $link = $items[0]->link;
      	echo "<div class='news'>";
        echo '<a href="' . $link . '">' . $title . '</a><br>';
        echo $description . "<br><br>\n";
        echo "<hr></div>";
      
	}
	?>
	
	
	
	