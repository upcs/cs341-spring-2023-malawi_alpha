#!/usr/bin/python3
import cgi
import connection
import os


def displayPrintout():
    # get the ID from the query string
    query_string = os.environ.get('QUERY_STRING', '')
    params = query_string.split('&')
    id_value = None
    for param in params:
        name, value = param.split('=')
        if name == 'ID':
            id_value = value
            break
    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl WHERE StudentID = " + id_value
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount

    if (queryResults > 0):

        for row in result:
            col_names = [desc[0] for desc in cursor.description]

            # School Information
            print("<table width=\"50%\" id=\"header-table\">")
            print("<tr>")
            print("<td class=\"header\">St. Mary's Karonga Girls Sec. School</td>")
            print("</tr>")
            print("<tr>")
            print("<td class=\"header\">PO Box 227</td>")
            print("</tr>")
            print("<tr>")
            print("<td class=\"header\">Karonga, Malawai</td>")
            print("</tr>")
            print("<tr>")
            print("<td class=\"header\"> <br></td>")
            print("<tr>")
            print("<td class=\"header\">Tel.: +265996541318</td>")
            print("</tr>")
            print("<tr>")
            print("<td class=\"header\">/+265880007813</td>")
            print("</tr>")
            print("<tr>")
            print(
                "<td class=\"header\">Email: stmaryskarongagirlssecondary@gmail.com</td>")
            print("</tr>")
            print("</table>")
            print("<table width=50% id=\"name-section\">")

            # Student Name
            print("<tr>")
            print("<td name=\"name-text\">", row[col_names.index(
                'FirstName')], " ", row[col_names.index('LastName')], "</td>")
            print("</tr>")
            print("</table>")

            print("<table width=50% id=\"grades-section\">")
            print("<th class = \"grades-header\" >SUBJECTS</th>")
            print("<th class = \"grades-header\" >MARKS(%)</th>")
            print("<th class = \"grades-header\" >GRADE</th>")
            print("<th class = \"grades-header\" >Position</th>")

            for col in col_names:

                data = row[col_names.index(col)]
                position = row[col_names.index('StudentPosition')]
                if data == None:
                    data = "&nbsp;"
                if position == None:
                    position = "&nbsp;"

                if col == 'StudentID' or col == 'FirstName' or col == 'LastName' \
                        or col == 'StudentPosition' or col == 'ClassID':
                    continue
                print("<tr class= grades-section>")
                print("<th class= \"student-data\"> ", col, "</th>")
                print("<td class= \"student-data\">Mark</td>")
                print("<td class= \"student-data\">", data, "</td>")
                print("<td class= \"student-data\">", position, "</td>")
                print("</tr>")

            print("</table>")
            print("<table class= \"comm-section\">")
            print("<tr>")
            print("<td class=\"footer\">Form Teacher Comments: </td>")
            print("</tr>")

            
            print("<tr>")
            print("<td class=\"footer\">Head Teacher Comments: </td>")
            print("</tr>")
            print("</table>")
            print("<br>")
    print("</table>")


print("Content-type: text/html")
print("")
print(open('single-printout.html').read())
displayPrintout()
