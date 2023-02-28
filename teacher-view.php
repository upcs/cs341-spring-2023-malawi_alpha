<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="utf-8" />
    <title>Testing</title>
    <link rel="stylesheet" href="teacher-view.css" />
</head>

<?php
// Function to handle "keydown" event on grade table cells
$doc = new DOMDocument();
$doc->loadHTMLFile("teacher-view.html");
function gradeCellHandler($event)
{
    if ($event['key'] === "Enter") {
        // Save changes and remove "contenteditable" attribute
        $newGrade = $event['target']['textContent'];
        $event['target']['removeAttribute']("contenteditable");
        $event['preventDefault'](); // Prevents the default behavior of adding a newline character
        $event['target']['setAttribute']("contenteditable", "true");
    }
}

// Define tokenButtonHandler function
function tokenButtonHandler($event)
{
    $token = $_POST['token-text'];
    $accessToken = "token";
    if ($token === $accessToken) {
        echo "<script>alert('You are now in edit mode. Click on a grade to edit it.');</script>";
        $tdList = document['querySelectorAll']("td.grades");
        // loop through the td elements and set their contenteditable property to true
        for ($i = 0; $i < count($tdList); $i++) {
            $tdList[$i]['setAttribute']("contenteditable", "true");
        }
    } else {
        echo "<script>alert('Invalid token. Please try again.');</script>";
    }
}

// Define printoutHandler function
function printoutHandler($event)
{
    header("Location: /printout.html");
}

// Define addNewStudent function
function addNewStudent($event)
{
    echo "<script>console.log('new student button clicked');</script>";
    $gradesheet = document['getElementById']("gradesheet-body");
    $length = count($gradesheet['rows']);
    $newRow = document['createElement']("tr"); // Create new row element
    for ($i = 0; $i < 20; $i++) {
        $newCell = document['createElement']("td"); // Create new cell element
        if ($i == 1) {
            $newCell['textContent'] = "Student " . $length;
        } else {
            $newCell['className'] = "grades";
        }
        $newRow['appendChild']($newCell); // Append the new cell to the new row
    }
    $gradesheet['appendChild']($newRow);
}

// Initialize script when document is ready
echo "<script>";
echo "$(function () {";

// Define PHP variables corresponding to JavaScript variables
echo "const gradesTds = document.querySelectorAll('.grades');";
echo "const tokenButton = document.getElementById('token-button');";
echo "const prinoutButton = document.getElementById('printout-button');";
echo "const gradesheet = document.getElementById('gradesheet-body');";
echo "const newStudentButton = document.getElementById('new-student-button');";

// Loop through grade table cells and add "keydown" event listener
echo "gradesTds.forEach((td) => {";
echo "  td.addEventListener('keydown', gradeCellHandler);";
echo "});";

// Add event listeners to buttons
echo "tokenButton.addEventListener('click', tokenButtonHandler);";
echo "prinoutButton.addEventListener('click', printoutHandler);";
echo "newStudentButton.addEventListener('click', addNewStudent);";

// Add default rows
echo "for(let i = 0; i < 10; i++){addNewStudent();}";

echo "});";
echo "</script>";
?>

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

    <div id="control-center">
        <textarea id="new-student" cols="30" rows="1"></textarea>
        <button type="submit" id="search-student-button">Search Student</button>

        <textarea id="token-text" cols="40" rows="1"></textarea>
        <button type="submit" id="token-button">Enter Token</button>

        <button type="submit" id="new-student-button">New Student</button>
        <button type="submit" id="printout-button">View Print Out</button>
    </div>

    <table width="100%" id="gradesheet">
        <tbody id="gradesheet-body">
            <tr>
                <td class="rotate-text">Class</td>
                <td class="rotate-text">Name</td>
                <td class="rotate-text">Position</td>
                <td class="rotate-text">Best of Five plus Eng</td>
                <td class="rotate-text">Running Average</td>
                <td class="rotate-text">POINTS</td>
                <td class="rotate-text">English</td>
                <td class="rotate-text">Physics</td>
                <td class="rotate-text">Chemistry</td>
                <td class="rotate-text">Biology</td>
                <td class="rotate-text">Maths</td>
                <td class="rotate-text">Social Studies</td>
                <td class="rotate-text">History</td>
                <td class="rotate-text">Geography</td>
                <td class="rotate-text">Agriculture</td>
                <td class="rotate-text">Bible Knowledge</td>
                <td class="rotate-text">Chichewa</td>
                <td class="rotate-text">French</td>
                <td class="rotate-text">Computer Studies</td>
                <td class="rotate-text">Life Skills</td>
            </tr>
        </tbody>
    </table>
<!-- Code injected by live-server -->
<script>
	// <![CDATA[  <-- For SVG support
	if ('WebSocket' in window) {
		(function () {
			function refreshCSS() {
				var sheets = [].slice.call(document.getElementsByTagName("link"));
				var head = document.getElementsByTagName("head")[0];
				for (var i = 0; i < sheets.length; ++i) {
					var elem = sheets[i];
					var parent = elem.parentElement || head;
					parent.removeChild(elem);
					var rel = elem.rel;
					if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
						var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
						elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
					}
					parent.appendChild(elem);
				}
			}
			var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
			var address = protocol + window.location.host + window.location.pathname + '/ws';
			var socket = new WebSocket(address);
			socket.onmessage = function (msg) {
				if (msg.data == 'reload') window.location.reload();
				else if (msg.data == 'refreshcss') refreshCSS();
			};
			if (sessionStorage && !sessionStorage.getItem('IsThisFirstTime_Log_From_LiveServer')) {
				console.log('Live reload enabled.');
				sessionStorage.setItem('IsThisFirstTime_Log_From_LiveServer', true);
			}
		})();
	}
	else {
		console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
	}
	// ]]>
</script>
</body>

</html>