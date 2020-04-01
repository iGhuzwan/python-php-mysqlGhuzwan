<html>

<head><title>Out Product Listing Project</title></head>

<body>

<h3>Some Extraordinary Products Listing:</h3>
<ol>
<?php
	$json = file_get_contents("http://dotcode.ml:3001/");
	$obj = json_decode($json);

	echo "$json";

?>
</ol>
</body>
</html>
