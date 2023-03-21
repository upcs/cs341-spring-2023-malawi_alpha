<?php

function newStudentButton()
{

	echo "<script>console.log('newStudentButton() called');</script>";
	// $dom = new DOMDocument();
	// $working = $dom->loadHTMLFile("/var/www/html/teacher-view.php");
	// if (!$working) {
	// 	echo "<script>console.log('DOMDocument failed to loadHTMLFile');</script>";
	// 	exit();
	// }

	// $tbody = $dom->getElementByid('gradesheet-body');
	// $len = count( $tbody->getElementsByTagName('tr'));

	// echo "<script>console.log('$len');</script>";

	// $new_row = $dom->createElement('tr');
	// for ($i = 0; $i < 20; $i++) {

	// 	echo "<script>console.log('$len $$$$ $i');</script>";

	// 	$new_cell = $dom->createElement('td');
	// 	if ($i == 1) {
	// 		$new_cell = $dom->createElement('td', "Student $len");
	// 	} else {
	// 		$new_cell->setAttribute('class', 'grades');
	// 	}
	// 	$new_row->appendChild($new_cell);
	// }

	// $tbody->appendChild($new_row);

	// $dom->saveHTMLFile("/var/www/html/teacher-view.php");
}

// $new_row = $dom->createElement('tr');

// for ($i = 0; $i < 20; $i++) {

//     $new_cell = $dom->createElement('td');
//     if($i == 1) {
//         $new_cell = $dom->createElement('td',"Student");
//     } else {
//         $new_cell->setAttribute('class','grades');
//     }
//     $new_row->appendChild($new_cell);
// }

// $gradesheet_body = $dom->getElementById("gradesheet-body");
// $gradesheet_body->appendChild($new_row);
// $gradesheet = $dom->getElementById("gradesheet");
//echo $dom->saveHTMLFile("/var/www/html/teacher-view.php");
// echo $dom->saveHTML();
?>