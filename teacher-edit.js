$(document).ready(function() {
  const $classSelect = $('#class-select');
  const $gradesheetHeader = $('#gradesheet-header');
  const $gradesheetBody = $('#gradesheet-body');

  function fetchGrades(selectedClass) {
    $.getJSON('/cgi-bin/get_grades.py', { class: selectedClass }, function(grades) {
      updateGradesheet(grades);
      });
  }

  function updateGradesheet(grades) {
      $gradesheetHeader.empty();
      $gradesheetBody.empty();

      $gradesheetHeader.append(`<tr><th>Name</th><th>Grade</th><th>Behavior</th></tr>`);

      $.each(grades, function(index, student) {
          $gradesheetBody.append(`<tr><td>${student.name}</td><td>${student.grade}</td><td>${student.behavior}</td></tr>`);
      });
  }

  $classSelect.on('change', function() {
      fetchGrades($(this).val());
  });

  // Initial load
  fetchGrades($classSelect.val());
});



/*
$(function () {
//change this to make a POST request to the server and get actual data
loadClass = function (event) {
    
  
    console.log("new student button clicked");
    let length = gradesheet.rows.length;
    var table_width = gradesheet.rows[0].cells.length;
    var newRow = document.createElement("tr"); // Create new row element
    for (var i = 0; i < table_width; i++) {
      var newCell = document.createElement("td"); // Create new cell element
      newCell.setAttribute("contenteditable", "true");
      if(i == 0) {
        newCell.innerText = "Student " + length;
      } else {
        newCell.className = "grades";
      }
      newRow.appendChild(newCell); // Append the new cell to the new row
    }
    gradesheet.appendChild(newRow);
    
  };
  
  //saving data to database
  const save_button = document.getElementById("save-button");
  save_button.addEventListener("click", function () {
  //TODO: make this actually save the data and verify database is updated 
   
    if(true){
      window.alert("Saved!");
    }else{
      window.alert("Not saved");
    }
  });
  
  
  for(let i = 0; i < 10; i++){loadClass()}
  const class_selector = document.getElementById("class-select");
  class_selector.addEventListener("change", function () {
    const selected_class = class_selector.value;
    var gradesheet_header = document.getElementById("gradesheet-header");
    gradesheet_header.innerText = selected_class;
    var gradesheet = document.getElementById("gradesheet");
    gradesheet.style.display = "block";
    save_button.style.display = "block";
    //add_student_button.style.display = "block";
  });
  
});
**/