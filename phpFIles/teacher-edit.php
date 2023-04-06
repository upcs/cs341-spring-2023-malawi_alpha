<?php
$gradesheet = $_POST['gradesheet'];
//function to add an editable student to the table
function addEditableStudent() {
    $gradesheet = $_POST['gradesheet'];
    echo "new student button clicked";
    $length = count($gradesheet);
    $table_width = count($gradesheet[0]);
    $newRow = "<tr>";
    for ($i = 0; $i < $table_width; $i++) {
        $newCell = "<td contenteditable='true'>";
        if ($i == 0) {
            $newCell .= "Student " . $length;
        } else {
            $newCell .= "<input type='text' class='grades'>";
        }
        $newCell .= "</td>";
        $newRow .= $newCell;
    }
    $newRow .= "</tr>";
    echo $newRow;
}

//add default rows
for ($i = 0; $i < 10; $i++) {
    addEditableStudent();
}

//event listener for add student button
if (isset($_POST['add-student'])) {
    addEditableStudent();
}

//event listener for save button
if (isset($_POST['save-button'])) {
    //TODO: save the data to the server and update the database
    if (true) {
        echo "<script>alert('Saved!');</script>";
    } else {
        echo "<script>alert('Not saved');</script>";
    }
}

//event listener for class selector
if (isset($_POST['class-select'])) {
    $selected_class = $_POST['class-select'];
    echo "<script>document.getElementById('gradesheet-header').innerText = '$selected_class';
        document.getElementById('gradesheet').style.display = 'block';
        document.getElementById('save-button').style.display = 'block';
        document.getElementById('add-student').style.display = 'block';</script>";
}

?>
