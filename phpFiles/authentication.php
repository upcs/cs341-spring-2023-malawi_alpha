<?php 

session_start(); 

include "connection.php";

// Checks to see if both fields were set if not then it redirects
if (isset($_POST['token'])) {

    function validate($data){

       $data = trim($data);

       $data = stripslashes($data);

       $data = htmlspecialchars($data);

       return $data;

    }

    $token = validate($_POST['token']);

    if (empty($token)) {

        header("Location: homepage.php?error=Token is required");

        exit();

    }else{
    	// Turns the entered token into a hash then checks to see if the token matches the login database
	$token = hash('ripemd160', $token);

        $sql = "SELECT * FROM tokenTbl WHERE token='$token'";

        $result = mysqli_query($con, $sql);

        if (mysqli_num_rows($result) == 1) {

            $row = mysqli_fetch_assoc($result);

            if ($row['token'] == $token) {

		// Sets a cookie that expires in 10 seconds so it's easier to check if cookie expires and works
                echo "Logged in!";
                setcookie("token", $row['token'], time() + 10);

                $_SESSION['token'] = $row['token'];


                $ID = mysqli_real_escape_string($con, $_GET['ID']);
                if (!isset($ID) || $ID == "") {
                	header("Location: newHomepage.php");
                }
                else {
                	header("Location: bidding.php?ID=".$ID."");
                }

                exit();

            }else{

                header("Location: index.php?error=Incorect User name or password");

                exit();

            }

        }else{

            header("Location: index.php?error=Incorect User name or password");

            exit();

        }

    }

}else{

    header("Location: index.php");

    exit();

}
