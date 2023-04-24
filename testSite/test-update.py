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
sql = "SELECT FirstName,LastName FROM GradeTbl"
cursor.execute(sql)
result = cursor.fetchall()
queryResults = cursor.rowcount
col_names = [desc[0] for desc in cursor.description]


data = {}

for key in dataset.keys():
    values = dataset.getlist(key)
    data[key] = values

success = True
for j in range(cursor.rowcount):
    currQuery = "UPDATE GradeTbl SET "
    for key in data.keys():
        toAdd = data[key][j]
        if key == 'StudentID':
            continue
        if toAdd == '.':
            toAdd = 'NULL'
        else:
            toAdd = toAdd.strip()
            toAdd = "'" + toAdd + "'"
        currQuery += " " + key + " = " + toAdd + ", "   
    currQuery = currQuery.rstrip(", ")  
    currQuery += " WHERE StudentID = " + str(j+1) + ";"
    # print(currQuery)
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
cursor.close()

