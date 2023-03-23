<!DOCTYPE html>

<?php
include 'connection.php';
?>

<html lang="en">

<head>
    <meta charset="utf-8" />
    <title id="title">Printout Page</title>
    <link rel="stylesheet" href="single-printout.css" />
</head>

<body>

    <?php

    $currID = $_GET['ID'];
    $sql = "SELECT * FROM GradeTbl WHERE StudentID = ". $currID;
    $result = mysqli_query($con, $sql);
    $queryResults = mysqli_num_rows($result);

    //Create table from sql query
    if ($queryResults > 0) {

        while ($row = mysqli_fetch_assoc($result)) {

            //School Information
            echo "<table width=\"50%\" id=\"header-table\">";
            echo "<tr>";
            echo "<td class=\"header\">St. Mary's Karonga Girls Sec. School</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class=\"header\">PO Box 227</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class=\"header\">Karonga, Malawai</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class=\"header\"> <br></td>";
            echo "<tr>";
            echo "<td class=\"header\">Tel.: +265996541318</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class=\"header\">/+265880007813</td>";
            echo "</tr>";
            echo "<tr>";
            echo "<td class=\"header\">Email: stmaryskarongagirlssecondary@gmail.com</td>";
            echo "</tr>";
            echo "</table>";
            echo "<table width=50% id=\"name-section\">";

            //Student Name
            echo "<tr>";
            echo "<td name=\"name-text\">" . $row['FirstName'] . " " . $row['LastName'] . "</td>";
            echo "</tr>";
            echo "</table>";

            //Header Table
            echo "<table width=50% id=\"grades-section\">";
            echo "<th class = \"grades-header\" >SUBJECTS</th>";
            echo "<th class = \"grades-header\" >MARKS(%)</th>";
            echo "<th class = \"grades-header\" >GRADE</th>";
            echo "<th class = \"grades-header\" >Position</th>";

            //Agriculture
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Agriculture</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Agriculture'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Bible Knowledge
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Bible Knowledge</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Bible Knowledge'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Biology 
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Biology</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Biology'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Chemistry
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Chemistry</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Chemistry'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Chichewa
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Chichewa</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Chichewa'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //English
    
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">English</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['English'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Geography
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Geography</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Geography'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //History
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">History</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['History'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Mathematics
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Mathematics</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Mathematics'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Physics
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Physics</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Physics'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Social Studies
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Social Studies</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Social Studies'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Social and Development Studies
            echo "<tr class= grades-section>";
            echo "<th class= \"student-data\">Social and Development Studies</th>";
            echo "<td class= \"student-data\">Mark</td>";
            echo "<td class= \"student-data\">" . $row['Social and Development Studies'] . "</td>";
            echo "<td class= \"student-data\">" . $row['StudentPosition'] . "</td>";
            echo "</tr>";

            //Form Teacher Comments
            echo "</table>";
            echo "<table class= \"comm-section\">";
            echo "<tr>";
            echo "<td class=\"footer\">Form Teacher Comments: </td>";
            echo "</tr>";

            //Head Teacher Comments
            echo "<tr>";
            echo "<td class=\"footer\">Head Teacher Comments: </td>";
            echo "</tr>";
            echo "</table>";
            echo "<br>";

        }
    } else {
        echo "0 results";
    }
    echo "</table>";
    ?>

</body>

</html>