<?php

session_start();


if (isset($_SESSION['token'])) {
	include 'connection.php';
	$query=mysqli_query($con, "SELECT * FROM tokenTbl WHERE token = '".$_SESSION['token']."'");
	$row = mysqli_fetch_assoc($query);
	$cookieUsername = $_COOKIE['token'];
	if (isset($cookieUsername)) {
		print("Cookie is valid\n");
		echo "<br>";
	}
	else {
		print("Cookie is expired please login again (WILL IMPLEMENT REDIRECTION TO LOGIN PAGE\n");
		echo "<br>";
	}
	print("Successful login");
}

?>
