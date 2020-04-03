<html>

<head><title>Connection via MariaDB</title></head>

<body>

<h3>MariaDB Database: </h3>
<ol>
<?php
	$json = file_get_contents("http://dotcode.ml:3001/");
	echo "Received from Python as JSON in PHP front-end PostgreSQL";
        echo "<li>$json</li>";
        $json = file_get_contents("http://dotcode.ml:3001/mariadb");
	echo "Received from Python as JSON in PHP front-end MariaDB";
        echo "<li>$json</li>";
      //  $json = file_get_contents("http://dotcode.ml:3001/mysqldb");
//	echo "Received from Python as JSON in PHP front-end MySQLDB";
  //      echo "<li>$json</li>";
?>
</ol>
</body>
</html>
