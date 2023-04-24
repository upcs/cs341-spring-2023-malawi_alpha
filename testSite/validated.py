#!/usr/bin/python3
import cgi
import connection
import os

def printEdit():

    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount

    print("<form method=\"post\" id=\"save-form\" name=\"save-form\">")
    print("<button type=\"submit\" id=\"save-button\" name=\"save-button\">Save Changes</button>")
    print("</form>")
    print("<br>")
    
    print("<table width=100%>")
    if (queryResults > 0):

        col_names = [desc[0] for desc in cursor.description]
        currID = -1
        firstName = -1
        lastName = -1

        print("<tr>")
        for col in col_names:
            if (col == "StudentID"):
                currID = col_names.index(col)
                continue
            elif (col == "FirstName"):
                firstName = col_names.index(col)
                continue
            elif (col == "LastName"):
                lastName = col_names.index(col)
                print("<th class = 'rotate-text'> Name </th>")
                continue
            print("<th class = 'rotate-text'>" + col + "</th>")

        for row in result:
            print("<tr>")
            for col in col_names:
                if (col == "StudentID" or col == "FirstName"):
                    continue
                elif (col == "LastName"):
                    print("<th><a href=teacher-edit.py?ID=" +
                          str(row[currID]) + ">", row[firstName], " ", row[lastName] + "</a></th>")
                    continue
                data = row[col_names.index(col)]
                if (data == None):
                    data = "&nbsp;"
                print("<td contenteditable=\"true\">" + data + "</td>")
            print("</tr>")
        print("</tr>")

    print("</table>")
    cursor.close()


query_string = os.environ.get('QUERY_STRING', '')
params = query_string.split('&')
id_value = None
for param in params:
    name, value = param.split('=')
    if name == 'ID':
        id_value = value
        break

    
print("Content-type: text/html")
print("")
print(open('teacher-view.html').read())
if id_value is None:
    print("No ID value")
elif id_value == '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5':  
    printEdit()
else:
    print("Invalid ID value")
