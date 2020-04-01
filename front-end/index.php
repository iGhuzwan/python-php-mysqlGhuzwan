<html>

<head><title>Out Product Listing Project</title></head>

<body>

<h3>Some Extraordinary Products Listing:</h3>
<ol>
<?php
	$json = file_get_contents("http://dotcode.ml:3001/");
	echo "Received from Python as JSON in PHP front-end";
        echo "<li>$json</li>";
        $obj = json_decode($json);
	echo "After JSON decode in PHP front-end";
        echo $obj->name;
	echo $obj->address;
?>
</ol>
</body>
</html>
