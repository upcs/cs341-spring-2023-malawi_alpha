<!DOCTYPE html>

<?php
use Symfony\Component\Console\Helper\TableCell;
use Symfony\Component\Console\Helper\TableRows;

require 'view-functionality.php';
include 'connection.php';

//if (isset($_COOKIE['token'])) {

  $pressed = false;
  


  if (isset($_POST['new-student-button'])) {
    newStudentButton();
  }

  $password = "token";
  if (isset($_POST['token-button'])) {
    unset($_POST['token-button']);
    $token = $_POST['token-text'];

    $pressed = true;
    if (strlen(trim($token)) == 0) {
      echo '<script>alert("Token is empty");</script>';
    } else {
      if (!preg_match('/^[a-zA-Z0-9]+$/', $token)) {
        echo '<script>alert("Token contains invalid characters");</script>';
      } else {
        if (strcmp($token, $password) == 0) {
          echo '<script>alert("Token is correct");</script>';
        } else {
          echo '<script>alert("Token is incorrect");</script>';
        }
      }
    }
    
  }
  

//}


?>

<html lang="en">

<head>
  <meta charset="utf-8" />
  <title id="title">Teacher Edit</title>
  <link rel="stylesheet" href="teacher-edit.css" />
</head>

<body>
  <form>
    <label for="class">Class</label>
    <select name="class" id="class">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
      <option value="6">6</option>
      <option value="7">7</option>
      <option value="8">8</option>
      <option value="9">9</option>
      <option value="10">10</option>
      <option value="11">11</option>
      <option value="12">12</option>
    </select>
    <label for="term">Term</label>
    <select name="term" id="term">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
    </select>
    <label for="year">Year</label>
    <select name="year" id="year">
      <option value="2021">2021</option>
      <option value="2022">2022</option>
      <option value="2023">2023</option>
      <option value="2024">2024</option>
      <option value="2025">2025</option>
      <option value="2026">2026</option>
      <option value="2027">2027</option>
      <option value="2028">2028</option>
      <option value="2029">2029</option>
      <option value="2030">2030</option>
    </select>
    <br /><br />
  </form>

  <form method="POST">
	  
	  <div class= "controlArea">
      <textarea class="edit-box" cols="30" rows="1" placeholder = "placeholder"></textarea> <br/>
	  <textarea class="edit-box" cols="30" rows="1" name="token-text" placeholder = "placeholder"></textarea> <br/>
	  <textarea class="edit-box" cols="30" rows="1" name="token-text" placeholder = "placeholder"></textarea> <br/>
	  <textarea class="edit-box" cols="30" rows="1" name="token-text" placeholder = "placeholder"></textarea> <br/>
	  <textarea class="edit-box" cols="30" rows="1" name="token-text" placeholder = "placeholder"></textarea>
      <button type="submit" id="update-grade-button">Update Grades</button>
	  
      <button type="submit" id="printout-button" name="printout-button">View Print Out</button>
      </div>
  </form>
  <?php
		
		$currentID = $_GET['ID'];
		$sql = "SELECT * FROM GradeTbl WHERE StudentID = ". $currentID;
		$result = mysqli_query($con, $sql);
		$queryResults = mysqli_num_rows($result);
		while($row = mysqli_fetch_assoc($result)) {
			echo "<h3 name=\"name-section\">"."".$row['FirstName']." ".$row['LastName']."'s grades</h3>";
		echo "<table>";
		if ($queryResults > 0) {
			echo "<tr>";
				echo "<th>Class</th>";
				echo "<td>".$row['ClassID']."</td>";
				echo "</tr><tr><th>Student Position</th>";
				echo "<td>".$row['StudentPosition']."</td>";
				echo "</tr><tr><th>Best of Five Plus English</th>";
				echo "<td>".$row['BOFPE']."</td>";
				echo "</tr><tr><th>Running Average</th>";
				echo "<td>".$row['RunningAverage']."</td>";
				echo "</tr><tr>";
				echo "<th>Points</th>";
				echo "<td>".$row['Points']."</td>";
				echo "</tr><tr>";
				echo "<th>English</th>";
				echo "<td>".$row['English']."</td>";
				echo "</tr><tr>";
				echo "<th>Physics</th>";
				echo "<td>".$row['Physics']."</td>";
				echo "</tr><tr>";
				echo "<th>Chemistry</th>";
				echo "<td>".$row['Chemistry']."</td>";
				echo "</tr><tr>";
				echo "<th>Biolody</th>";
				echo "<td>".$row['Biology']."</td>";
				echo "</tr><tr>";
				echo "<th>Math</th>";
				echo "<td>".$row['Math']."</td>";
				echo "</tr><tr>";
				echo "<th>Social Studies</th>";
				echo "<td>".$row['SocialStudies']."</td>";
				echo "</tr><tr>";
				echo "<th>History</th>";
				echo "<td>".$row['History']."</td>";
				echo "</tr><tr>";
				echo "<th>Geography</th>";
				echo "<td>".$row['Geography']."</td>";
				echo "</tr><tr>";
				echo "<th>Agriculture</th>";
				echo "<td>".$row['Agriculture']."</td>";
				echo "</tr><tr>";
				echo "<th>Bible Knowledge</th>";
				echo "<td>".$row['BibleKnowledge']."</td>";
				echo "</tr><tr>";
				echo "<th>Chichewa</th>";
				echo "<td>".$row['Chichewa']."</td>";
				echo "</tr><tr>";
				echo "<th>French</th>";
				echo "<td>".$row['French']."</td>";
				echo "</tr><tr>";
				echo "<th>Computer Studies</th>";
				echo "<td>".$row['ComputerStudies']."</td>";
				echo "</tr><tr>";
				echo "<th>Life Skills</th>";
				echo "<td>".$row['LifeSkills']."</td>";
				echo "</tr>";
			}
		}
		echo "</table>";

    if (isset($_POST['printout-button'])) {
      // Redirect the user to printout.php
      
      header("Location: single-printout.php?ID=$currentID", true);
      exit();
    }
?>

	
</body>

</html>
