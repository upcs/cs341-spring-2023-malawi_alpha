<?php

$dom = new DOMDocument();
$working = $dom->loadHTMLFile("/var/www/html/teacher-view.php");

if($working) {
    echo "Still working";
} else {
    echo "Stopped working";
}


$new_row = $dom->createElement('tr');

for ($i = 0; $i < 20; $i++) {
    
    $new_cell = $dom->createElement('td');
    if($i == 1) {
        $new_cell = $dom->createElement('td',"Student");
    } else {
        $new_cell->setAttribute('class','grades');
    }
    $new_row->appendChild($new_cell);
}

$gradesheet_body = $dom->getElementById("gradesheet-body");
$gradesheet_body->appendChild($new_row);
$gradesheet = $dom->getElementById("gradesheet");
echo $dom->saveHTML();
?>
