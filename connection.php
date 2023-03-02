<!-- change host user and password -->
<?php
    $host = "10.12.116.141";
    $user = "malawiTest";
    $password = 'test';
    $db_name = "testMalawi";

    $con = mysqli_connect($host, $user, $password, $db_name);
    if(mysqli_connect_errno()) {
        die("Failed to connect with MySQL: ". mysqli_connect_error());
    }
?>