<!DOCTYPE html>

<html lang="en">
<head>
    <title>Add New Student</title>
</head>

<body>
    <form method="POST">
        <label for="student-first">First Name</label>
        <input type="text" id="student-first" name="student-first" />

        <label for="student-last">Last Name</label>
        <input type="text" id="student-last" name="student-last" />

        <label for="student-mark">Student Mark</label>
        <input type="text" id="student-mark" name="student-mark" />

        <button type="submit" id="add-student-button" name="add-student-button">Add Student</button>
        <button type="submit" id="return-button" name="return-button">Return to Teacher View</button>
        
    </form>

    </html>

<?php
include 'connection.php';

if (isset($_POST['add-student-button'])) {
    
    $first = $_POST['student-first'];
    $last = $_POST['student-last'];
    $mark = $_POST['student-mark'];

    if (empty($first) || empty($last) || $first == "" || $last == "") {
        echo "<script> alert(\"Please fill in all fields\")</script>";
        exit();
    } else {
        $sql = "SELECT COUNT(StudentID) FROM StudentTbl";
        $result = mysqli_query($con, $sql);
        $count = mysqli_fetch_row($result)[0];
        $num_rows = $count + 1;
        $sql = "INSERT INTO StudentTbl(StudentID, FirstName, LastName, Mark) VALUES('$num_rows', '$first', '$last', NULL)";
        mysqli_query($con, $sql);
        echo "<script> alert(\"Student Added\")</script>";
    }
    
    
}

if (isset($_POST['return-button'])) {
    header("Location: teacher-view.php");
    exit();
}


?>
</body>
</html>
