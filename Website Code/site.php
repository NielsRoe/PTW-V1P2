<!DOCTYPE html>
<html>
<head>

	<title>Container Dashboard</title>
	<link rel="stylesheet" type="text/css" href="index.css?v=1.1">
	<link rel="shortcut icon" type="image/png" href="headerIcon.png"/>
	<link rel="stylesheet" href="classes.css">
	<link rel="stylesheet" href="table.css">
	<meta http-equiv="refresh" content="15">
	
</head>
<body>

	<div class="navbar">
		<div class="navcontent">
			<div class="info">
				<font size="+3">
					<b>Container Dashboard // Utrecht // De Uithof</b>
				</font>
			</div>
		</div>
	</div>

<div class="main">
<center>
<img src="bgImage.png" alt="Trashpile">
</center>
</div>

<?php
   $host        = "host = 127.0.0.1";
   $port        = "port = 5432";
   $dbname      = "dbname = Vuilcontainers";
   $credentials = "user = postgres password=0000";

   $db = pg_connect( "$host $port $dbname $credentials"  );
##   if(!$db) {
##      echo "Error : Unable to open database!";
##  } else {
##      echo "Opened database successfully!";
##   }

//Request results with a query
$result = pg_query("SELECT * FROM trashbins");
  
?>

<div class="main1">
</div>

	<div class="main2">
		<div class="tables" id="t">
<table id="cinfo">

    <thead>
    <tr>
        <th>Container ID</th>
        <th>Plaats</th>
        <th>Straat</th>
        <th>Vol</th>
    </tr>
    </thead>
    <tbody>
    <!--Use a while loop to make a table row for every DB row-->
    <?php while ($row = pg_fetch_assoc($result)) { ?>
        <tr>
            <!--Echo table columns into table cells-->
            <td><?php echo $row["trashbin_id"]; ?></td>
            <td><?php echo $row["city"]; ?></td>
            <td><?php echo $row["street"]; ?></td>
            <td><?php echo $row["filled"]; ?></td>
        </tr>
    <?php } ?>
    </tbody>
</table>
</div>
</div>

<div class="main1">
</div>

	<div class="main3">

		<div id="googlemaps">
			<iframe src="https://www.google.com/maps/d/u/0/embed?mid=1y4YDaofHbvkEL4tfL73yVXLuij4dhRLd"
			width="1080" height="480"></iframe>
		</div>
	</div>
	
<div class="main1">
</div>

<div class="footer">
	<div class="info">
		<font size="+1">
			<b><i>Januari 2019 // PTW // V1P Groep 2</i></b>
		</font>
	</div>
	<div class="info">
		<i>Website created by Thom Pestman & Niels Roeleveld</i>
	</div>
</div>

</body>
</html>