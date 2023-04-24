#!/usr/bin/python3
import connection

def displayPrinout():
    
    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    col_names = [desc[0] for desc in cursor.description]
    
    print('<div class="parent-container">')
    if(queryResults > 0):
            for row in result:
                print('<div class="student-container">')
                print("<table id=\"header-table\">")
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
                print("<td class=\"header\">Email: stmaryskarongagirlssecondary@gmail.com</td>")
                print("</tr>")
                print("</table>")

                # # Student Name
                firstName = str(row[col_names.index("FirstName")])
                lastName = str(row[col_names.index("LastName")])    
                print("<table id=\"name-section\">")
                print("<tr>")
                print("<td>" + firstName + " " + lastName + "</td>")
                print("</tr>")
                print("</table>")
                    
                # Header Table
                print("<table id=\"grades-section\">")
                print("<th class = \"grades-header\" >SUBJECTS</th>")
                print("<th class = \"grades-header\" >MARKS(%)</th>")
                print("<th class = \"grades-header\" >GRADE</th>")
                print("<th class = \"grades-header\" >Position</th>")
        
                for col in col_names:
                    if(col == "StudentID" or col == "FirstName" or col == "LastName" or col == "StudentClass"):
                        continue
                    
                    data = str(row[col_names.index(col)])
                    student_pos = str(row[col_names.index("StudentPosition")])
                    if student_pos == "None":
                        student_pos = "&nbsp;"
                    if(data == "None"):
                        data = "&nbsp;"
                    print("<tr class= grades-section>")
                    print("<th class= \"student-data\">", col , "</th>")
                    print("<td class= \"student-data\">",data,"</td>")
                    print("<td class= \"student-data\"></td>")
                    print("<td class= \"student-data\">"+ student_pos + "</td>")
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

                print("</table>") # End of the whole table
                print("<br>")
                print('</div>')
    print('</div>')
    cursor.close()    
print("Content-type: text/html")
print("")
print(open("all-printout.html").read())
displayPrinout()
