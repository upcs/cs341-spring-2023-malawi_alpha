#!/usr/bin/python3
import cgi
import connection

print('Content-type: text/html\r')
print("")
print("<h1>Update Grades</h1>")
print("<form method=\"post\" action=\"testing_newtable.py\">")
print("<button type=\"submit\" id=\"return-button\">Return</button >")
print("</form >")

dataset = cgi.FieldStorage()
cursor = connection.connect()

data = {}

for key in dataset.keys():
    values = dataset.getlist(key)
    data[key] = values

success = True
student_ids = data['StudentID']

for i, student_id in enumerate(student_ids):
    currQuery = "UPDATE GradeTbl SET "
    for key in data.keys():
        if key == 'StudentID':
            continue
        toAdd = data[key][i]
        if toAdd == '.':
            toAdd = 'NULL'
        else:
            toAdd = toAdd.strip()
            # toAdd = "'" + toAdd + "'"
        currQuery += " " + key + " = " + toAdd + ", "
    currQuery = currQuery.rstrip(", ")
    currQuery += " WHERE StudentID = " + student_id + ";"
    try:
        cursor.execute(currQuery)
        cursor.connection.commit()
    except Exception as e:
        print("Error executing query: ", e)
        print("Return to page and try again.")
        cursor.connection.rollback()
        cursor.close()
        success = False
        break

if success:
    print("Grades updated successfully.")
    print("Click the button to return to the main page.")
else:
    print("Grades were not updated successfully.")
    print("Click the button to return to the main page.")
cursor.close()

