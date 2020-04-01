<html>

<head><title>Out Product Listing Project</title></head>

<body>

<h3>Some Extraordinary Products Listing:</h3>
<ol>
<?php
	$json = file_get_contents("http://dotcode.ml:3001/");
	echo "<li>$json</li>";
        $obj = json_decode($json);
        echo "<li>$obj</li>";
        $products = $obj;

	foreach ($products as $product){
		echo "<li>$product</li>";
	}

?>
</ol>
</body>
</html>
