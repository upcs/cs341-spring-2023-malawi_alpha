$(function () {
  var tdList = document.querySelectorAll("td.grades");
  // loop through the td elements and set their contenteditable property to true
  for (var i = 0; i < tdList.length; i++) {
    tdList[i].setAttribute("contenteditable", "true");
  }
  // When a cell is edited, send the new data to the server
  $("td[contenteditable]").on("blur", function () {
    var cell = $(this);
    var row = cell.closest("tr");
    var data = {
      column: cell.index(),
      value: cell.text(),
    };
    // Send an AJAX request to the server to save the data
    $.ajax({
      url: "/save-data",
      method: "POST",
      data: data,
      success: function (response) {
        console.log("Data saved successfully");
      },
      error: function (xhr, status, error) {
        console.error("Error saving data:", error);
      },
    });
  });

  const gradesTds = document.querySelectorAll(".grades");
  // Add event listener for "keydown" on each td element
  gradesTds.forEach((td) => {
    td.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        // Save changes and remove "contenteditable" attribute
        const newGrade = td.innerText;
        td.removeAttribute("contenteditable");
        event.preventDefault(); // Prevents the default behavior of adding a newline character
        td.setAttribute("contenteditable", "true");
      }
    });
  });

  let gradesheet = document.getElementById("gradesheet");
  
});
