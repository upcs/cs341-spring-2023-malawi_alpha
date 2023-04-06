import logging
import random

# set up logging
logging.basicConfig(level=logging.INFO)

def token_entry_handler(event):
    input_token = input("Enter token: ")
    admin_token = "tempToken"
    logging.info(admin_token)
    logging.info(input_token)

    if input_token == admin_token:
        logging.info("Token is correct, you are now in editing mode. Don't forget to save before closing.")
        # open everything to be in editing mode, UNLOCK THE PAGE 
        # use should be able to edit token, teachers, classes
        # add classes and teachers for newly generated token 
        # additionally delete tokens, new collumn with delete token button will appear for all tokens 

        # be able to generate new token if the adminToken was correct
        def generate_token_handler(event):
            new_token = random.randint(100000, 999999)  # randomly generate 6 digit number for new token
            logging.info(new_token)

            # add new row to the table and new token into the first cell
            def new_row():

                #How do i access the table with python????
                table = document.getElementById("tokensheet")
                row = table.insertRow(1)
                cell1 = row.insertCell(0)
                cell2 = row.insertCell(1)
                cell3 = row.insertCell(2)
                cell1.innerHTML = new_token
                cell2.innerHTML = placeholder="Add classes for this token"
                cell3.innerHTML = placeholder="Add teacher using this token"

            new_row()

        # Be able to save changes if the adminToken was correct
        def save_button_handler(event):
            logging.info("Save button clicked")
            logging.info("All changes have been saved, it is now safe to exit.")

        generate_token_button = input("Press enter to generate a new token")
        save_button = input("Press enter to save changes")

        if generate_token_button:
            generate_token_handler(event)

        if save_button:
            save_button_handler(event)

    if input_token != admin_token:
        logging.info("Token is incorrect, please try again.")

# set up event listeners
token_entry = input("Press enter to enter a token")
token_entry.addEventListener("change", token_entry_handler)
