$(function(){

    const tokenEntry = document.getElementById("token-entry");
    const generateTokenButton = document.getElementById("generate-token-button");
    const saveButton = document.getElementById("save-button");

    tokenEntryHandler = function(event){
        var inputToken = $("#token-entry").val();
        const adminToken = "tempToken";
        console.log(adminToken);
        console.log(inputToken);
        if(inputToken === adminToken){
            window.alert("Token is correct, you are now in editing mode. Don't forget to save before closing.");
            //open everything to be in editing mode, UNLOCK THE PAGE 
            //use should be able to edit token, teachers, classes
            //add classes and teachers for newly generated token 
            //additionally delete tokens, new collumn with delete token button will appear for all tokens 

            //be able to generate new token if the adminToken was correct
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
                    cell1.innerHTML = newToken;
                    cell2.innerHTML = placeholder="Add classes for this token";
                    cell3.innerHTML = placeholder="Add teacher using this token";
                }
                newRow();

            }
            generateTokenButton.addEventListener("click", generateTokenHandler);
            
            //Be able to save changes if the adminToken was correct
            saveButtonHandler = function (event){
                console.log("Save button clicked");
                window.alert("All changes have been saved, it is now safe to exit.");
            }
            saveButton.addEventListener("click", saveButtonHandler);
        }
        if(inputToken != adminToken){
            window.alert("Token is incorrect, please try again.");
        }
    };

    saveButtonHandler = function (event){
        console.log("Save button clicked");
        window.alert("All changes have been saved, it is now safe to exit.");
    }

    tokenEntry.addEventListener("change", tokenEntryHandler);
    //generateTokenButton.addEventListener("click", generateTokenHandler);
    //saveButton.addEventListener("click", saveButtonHandler);
});