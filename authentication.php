<?php

session_start();

include "connection.php";

//checks to see if field is empty

if (isset($_POST['token'])) {
    // Creates validation function
    function validate($data)
    {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    $token = validate($_POST['token']);
    $token = hash('ripemd160', $token);
    $sql = "SELECT * FROM TokenTbl WHERE Token = '$token'";
    $result = mysqli_query($con, $sql);
    $numRows = mysqli_num_rows($result);
    if ($numRows == 1) {
        $currentRow = mysqli_fetch_assoc($result);
        echo "Logged in!";
        setcookie("Token", $currentRow['Token'], time() + 10);
        $_SESSION['Token'] = $currentRow['Token'];

        if ($currentRow['UserType'] == "teacher") {
            header("Location: teacher-view.php");
        } else if ($currentRow['UserType'] == "admin") {
            header("Location: admin-view.php");
        }

    } else {
        header("Location: index.php?error=Incorrect Token or more than 2 tokens exist");
        exit();
    }
} else {

    header("Location: index.html");

    exit();

}
?>