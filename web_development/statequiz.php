<html>
<head>
  <title>State Capital Quiz</title>
  <style>
  	body {background-color: lightblue; font-family: helvetica;}
  	input, legend {font-size: 150%;}
	select, option {font-size: 400%;}
	.mybutton {
		font-size: 250%;
		background-color: orange;
	}
	.mymenu {
		font-size: 250%;
		background-color: orange;
	}

  </style>
</head>
<body>
<?php # set up capitals array
$capitals = array(
"Afghanistan" => "Kabul",
"Albania" => "Tirane",
"Algeria" => "Algiers",
"Andorra" => "Andorra la Vella",
"Angola" => "Luanda",
"Antigua and Barbuda" => "Saint John's",
"Argentina" => "Buenos Aires",
"Armenia" => "Yerevan",
"Australia" => "Canberra",
"Austria" => "Vienna",
"Azerbaijan" => "Baku",
"The Bahamas" => "Nassau",
"Bahrain" => "Manama",
"Bangladesh" => "Dhaka",
"Barbados" => "Bridgetown",
"Belarus" => "Minsk",
"Belgium" => "Brussels",
"Belize" => "Belmopan",
"Benin" => "Porto-Novo",
"Bhutan" => "Thimphu",
"Bolivia" => "La Paz (administrative) Sucre (judicial)",
"Bosnia and Herzegovina" => "Sarajevo",
"Botswana" => "Gaborone",
"Brazil" => "Brasilia",
"Brunei" => "Bandar Seri Begawan",
"Bulgaria" => "Sofia",
"Burkina Faso" => "Ouagadougou",
"Burundi" => "Bujumbura",
"Cambodia" => "Phnom Penh",
"Cameroon" => "Yaounde",
"Canada" => "Ottawa",
"Cape Verde" => "Praia",
"Central African Republic" => "Bangui",
"Chad" => "N'Djamena",
"Chile" => "Santiago",
"China" => "Beijing",
"Colombia" => "Bogota",
"Comoros" => "Moroni",
"Congo, Republic of the" => "Brazzaville",
"Congo, Democratic Republic of the" => "Kinshasa",
"Costa Rica" => "San Jose",
"Cote d'Ivoire" => "Yamoussoukro (official) Abidjan (de facto)",
"Croatia" => "Zagreb",
"Cuba" => "Havana",
"Cyprus" => "Nicosia",
"Czech Republic" => "Prague",
"Denmark" => "Copenhagen",
"Djibouti" => "Djibouti",
"Dominica" => "Roseau",
"Dominican Republic" => "Santo Domingo",
"East Timor" => "Dili",
"Ecuador" => "Quito",
"Egypt" => "Cairo",
"El Salvador" => "San Salvador",
"Equatorial Guinea" => "Malabo",
"Eritrea" => "Asmara",
"Estonia" => "Tallinn",
"Ethiopia" => "Addis Ababa",
"Fiji" => "Suva",
"Finland" => "Helsinki",
"France" => "Paris",
"Gabon" => "Libreville",
"The Gambia" => "Banjul",
"Georgia" => "Tbilisi",
"Germany" => "Berlin",
"Ghana" => "Accra",
"Greece" => "Athens",
"Grenada" => "Saint George's",
"Guatemala" => "Guatemala City",
"Guinea" => "Conakry",
"Guinea-Bissau" => "Bissau",
"Guyana" => "Georgetown",
"Haiti" => "Port-au-Prince",
"Honduras" => "Tegucigalpa",
"Hungary" => "Budapest",
"Iceland" => "Reykjavik",
"India" => "New Delhi",
"Indonesia" => "Jakarta",
"Iran" => "Tehran",
"Iraq" => "Baghdad",
"Ireland" => "Dublin",
"Israel" => "Jerusalem",
"Italy" => "Rome",
"Jamaica" => "Kingston",
"Japan" => "Tokyo",
"Jordan" => "Amman",
"Kazakhstan" => "Astana",
"Kenya" => "Nairobi",
"Kiribati" => "Tarawa",
"Korea, North" => "Pyongyang",
"Korea, South" => "Seoul",
"Kuwait" => "Kuwait City",
"Kyrgyzstan" => "Bishkek",
"Laos" => "Vientiane",
"Latvia" => "Riga",
"Lebanon" => "Beirut",
"Lesotho" => "Maseru",
"Liberia" => "Monrovia",
"Libya" => "Tripoli",
"Liechtenstein" => "Vaduz",
"Lithuania" => "Vilnius",
"Luxembourg" => "Luxembourg",
"Macedonia" => "Skopje",
"Madagascar" => "Antananarivo",
"Malawi" => "Lilongwe",
"Malaysia" => "Kuala Lumpur",
"Maldives" => "Male",
"Mali" => "Bamako",
"Malta" => "Valletta",
"Marshall Islands" => "Majuro",
"Mauritania" => "Nouakchott",
"Mauritius" => "Port Louis",
"Mexico" => "Mexico City",
"Federated States of Micronesia" => "Palikir",
"Moldova" => "Chisinau",
"Monaco" => "Monaco",
"Mongolia" => "Ulaanbaatar",
"Montenegro" => "Podgorica",
"Morocco" => "Rabat",
"Mozambique" => "Maputo",
"Myanmar (Burma)" => "Rangoon but moving to Pyinmana",
"Namibia" => "Windhoek",
"Nauru" => "no official capital; government offices in Yaren District",
"Nepal" => "Kathmandu",
"Netherlands" => "Amsterdam",
"New Zealand" => "Wellington",
"Nicaragua" => "Managua",
"Niger" => "Niamey",
"Nigeria" => "Abuja",
"Norway" => "Oslo",
"Oman" => "Muscat",
"Pakistan" => "Islamabad",
"Palau" => "Koror",
"Panama" => "Panama City",
"Papua New Guinea" => "Port Moresby",
"Paraguay" => "Asuncion",
"Peru" => "Lima",
"Philippines" => "Manila",
"Poland" => "Warsaw",
"Portugal" => "Lisbon",
"Qatar" => "Doha",
"Romania" => "Bucharest",
"Russia" => "Moscow",
"Rwanda" => "Kigali",
"Saint Kitts and Nevis" => "Basseterre",
"Saint Lucia" => "Castries",
"Saint Vincent and the Grenadines" => "Kingstown",
"Samoa" => "Apia",
"San Marino" => "San Marino",
"Sao Tome and Principe" => "Sao Tome",
"Saudi Arabia" => "Riyadh",
"Senegal" => "Dakar",
"Serbia" => "Belgrade",
"Seychelles" => "Victoria",
"Sierra Leone" => "Freetown",
"Singapore" => "Singapore",
"Slovakia" => "Bratislava",
"Slovenia" => "Ljubljana",
"Solomon Islands" => "Honiara",
"Somalia" => "Mogadishu",
"South Africa" => "Pretoria (administrative) Cape Town (legislative) Bloemfontein (judiciary)",
"Spain" => "Madrid",
"Sri Lanka" => "Colombo",
"Sudan" => "Khartoum",
"Suriname" => "Paramaribo",
"Swaziland" => "Mbabana",
"Sweden" => "Stockholm",
"Switzerland" => "Bern",
"Syria" => "Damascus",
"Tajikistan" => "Dushanbe",
"Tanzania" => "Dar es Salaam",
"Thailand" => "Bangkok",
"Togo" => "Lome",
"Tonga" => "Nuku'alofa",
"Trinidad and Tobago" => "Port-of-Spain",
"Tunisia" => "Tunis",
"Turkey" => "Ankara",
"Turkmenistan" => "Ashgabat",
"Tuvalu" => "Funafuti",
"Uganda" => "Kampala",
"Ukraine" => "Kyiv",
"United Arab Emirates" => "Abu Dhabi",
"United Kingdom" => "London",
"United States" => "Washington D.C.",
"Uruguay" => "Montevideo",
"Uzbekistan" => "Tashkent",
"Vanuatu" => "Port-Vila",
"Vatican City (Holy See)" => "Vatican City",
"Venezuela" => "Caracas",
"Vietnam" => "Hanoi",
"Yemen" => "Sanaa",
"Zambia" => "Lusaka",
"Zimbabwe" => "Harare");

	if ( isset( $_GET['country'] ) ) {
		handleform($capitals);
	}
	displayform($capitals);

?>
<br>
</body>
</html>
<?php
function handleform($capitals){
      if (isset($_GET["country"])) { // check the pull-down
          $country = $_GET['country'];
          echo "<fieldset>
          			<legend>The capital of $country is </legend>
          			<h1>" . $capitals[$country]. "</h1>
          		</fieldset>";
      }
}

function displayform($list){
?>
	<fieldset><legend>Select a country, I'll show you the capital:</legend>
		<form method="get">
			<?php createmenu($list, "country"); ?>
    		<input class="mybutton" value="Take That!" type="submit">
		</form>
	</fieldset>
<?php
}

function createmenu($list, $name){
	echo "<select name='country' class='mymenu'>";

	foreach($list as $key => $value) {
		echo "<option>$key</option>";
	}
	echo "</select>";
}

