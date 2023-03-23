<!DOCTYPE html>

<?php
use Symfony\Component\Console\Helper\TableCell;
use Symfony\Component\Console\Helper\TableRows;

require 'view-functionality.php';
include 'connection.php';

//if (isset($_COOKIE['token'])) {

  $pressed = false;
  if (isset($_POST['printout-button'])) {
    // Redirect the user to printout.php
    header("Location: all-printout.php", true);
    exit();
  }


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
  <title id="title">Teacher View</title>
  <link rel="stylesheet" href="teacher-view.css" />
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
    <div id="control-center">
      <textarea id="new-student" cols="30" rows="1"></textarea>
      <button type="submit" id="search-student-button">Search Student</button>

      <textarea id="token-text" cols="40" rows="1" name="token-text"></textarea>
      <button type="submit" id="token-button" name="token-button">Enter Token</button>
      <button type="submit" id="new-student-button" name="new-student-button">New Student</button>
      <button type="submit" id="printout-button" name="printout-button">View Print Out</button>
    </div>
  </form>
  <?php
		$sql = "SELECT * FROM GradeTbl";
		$result = mysqli_query($con, $sql);
		$queryResults = mysqli_num_rows($result);
    $curr = 1;
		echo "<table width='100%'>";
		if ($queryResults > 0) {
			echo "<tr>";
				echo "<th class = 'rotate-text'>Class</th>";
				echo "<th class = 'rotate-text'>Name</th>";
				echo "<th class = 'rotate-text'>Position</th>";
				echo "<th class = 'rotate-text'>Best of Five plus Eng</th>";
				echo "<th class = 'rotate-text'>Running Average</th>";
				echo "<th class = 'rotate-text'>POINTS</th>";
				echo "<th class = 'rotate-text'>English</th>";
				echo "<th class = 'rotate-text'>Physics</th>";
				echo "<th class = 'rotate-text'>Chemistry</th>";
				echo "<th class = 'rotate-text'>Biology</th>";
				echo "<th class = 'rotate-text'>Maths</th>";
				echo "<th class = 'rotate-text'>Social Studies</th>";
				echo "<th class = 'rotate-text'>History</th>";
				echo "<th class = 'rotate-text'>Geography</th>";
				echo "<th class = 'rotate-text'>Agriculture</th>";
				echo "<th class = 'rotate-text'>Bible Knowledge</th>";
				echo "<th class = 'rotate-text'>Chichewa</th>";
				echo "<th class = 'rotate-text'>French</th>";
				echo "<th class = 'rotate-text'>Computer Studies</th>";
				echo "<th class = 'rotate-text'>Life Skills</th>";
				echo "</tr>";
			while($row = mysqli_fetch_assoc($result)) {
				echo "<tr>";
				echo "<td>".$row['ClassID']."</td>";
				echo "<th name=\"teacher-edit.php?ID=$curr\">"."<a href='teacher-edit.php?ID=".$row['StudentID']."'>".$row['FirstName']." ".$row['LastName']."</a></th>";
        $curr = $curr + 1;
				echo "<td>".$row['StudentPosition']."</td>";
				echo "<td>".$row['BOFPE']."</td>";
				echo "<td>".$row['RunningAverage']."</td>";
				echo "<td>".$row['Points']."</td>";
				echo "<td>".$row['English']."</td>";
				echo "<td>".$row['Physics']."</td>";
				echo "<td>".$row['Chemistry']."</td>";
				echo "<td>".$row['Biology']."</td>";
				echo "<td>".$row['Math']."</td>";
				echo "<td>".$row['SocialStudies']."</td>";
				echo "<td>".$row['History']."</td>";
				echo "<td>".$row['Geography']."</td>";
				echo "<td>".$row['Agriculture']."</td>";
				echo "<td>".$row['BibleKnowledge']."</td>";
				echo "<td>".$row['Chichewa']."</td>";
				echo "<td>".$row['French']."</td>";
				echo "<td>".$row['ComputerStudies']."</td>";
				echo "<td>".$row['LifeSkills']."</td>";
				echo "</tr>";
			}
		}
		echo "</table>";
?>

	
</body>

</html>
