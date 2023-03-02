$(function(){

    const editTokenButton = document.getElementById("edit-token-button");
    const generateTokenButton = document.getElementById("generate-token-button");
    const saveButton = document.getElementById("save-button");

    editTokenHandler = function (event){
        var adminToken = $("#token-entry").val();
        const adminToken = "tempToken";
        console.log(adminToken);
        console.log(inputToken);
        if(token == inputToken){
            console.alert("Token is correct, you are now in editing mode. Don't forget to save before closing.");
            //be able to edit the cells, add classes into the classes collum, and edit the teacher collumn 

        }
        else{
            console.alert("Token is incorrect, please try again.");
        }

    };

    generateTokenHandler = function (event){
        var newToken = Math.floor(Math.random() * 899999 + 100000)     //randomly generate 6 digit number for new token
        console.log(newToken);
        var table = document.getElementById("tokensheet");


        //add new row to the table and new token into the first cell
        function newRow(){
            var row = table.insertRow(1);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);
            cell1.innerHTML = print(newToken);
            cell2.innerHTML = "New Cell2";
            cell3.innerHTML = "New Cell3";
        }
    };

    //pushing to personal branch
    saveButtonHandler = function (event){
        console.log("Save button clicked");
        console.alert("All changes have been saved, it is now safe to exit.");
    }


    editTokenButton.addEventListener("click", editTokenHandler);
    generateTokenButton.addEventListener("click", generateTokenHandler);
    saveButton.addEventListener("click", saveButtonHandler);
});