#!/usr/bin/python3
import cgi
import connection


def printTable():

    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    print("<form method=\"post\" action=\"test-update.py\">")
    print("<button type=\"submit\" id=\"update-grade-button\" action=\"update-grades.py\">Update Grades</button >")

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
                data = str(row[col_names.index(col)])
                if (data == "None"):
                    data = "&nbsp;"
                print("<td><textarea class=\"grade-edit-box\" name=\"" + col +
                      "\" id=\"" + col + "\" cols=\"30\" rows=\"1\">", data, "</textarea></td>")
            print("</tr>")
        print("</tr>")

    print("</table>")
    print("</form >")
    cursor.close()


print("Content-type: text/html")
print("")
print(open('teacher-view.html').read())
printTable()
