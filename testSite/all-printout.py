#!/usr/bin/python3
import connection

def displayPrinout():
    
    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    
    if(queryResults > 0):

        for row in result:
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
            print("<td class=\"header\">Email: stmaryskarongagirlssecondary@gmail.com</td>")
            print("</tr>")
            print("</table>")

            # Student Name
            firstName = str(row[2])
            lastName = str(row[3])    
            print("<table width=\"50%\" id=\"name-section\">")
            print("<tr>")
            print("<td>" + firstName + " " + lastName + "</td>")
            print("</tr>")
            print("</table>")
            
            studentPosition = row[4]
            if(studentPosition is None):
                studentPosition = "&nbsp"
                
            # Header Table
            print("<table width=\"50%\" id=\"grades-section\">")
            print("<th class = \"grades-header\" >SUBJECTS</th>")
            print("<th class = \"grades-header\" >MARKS(%)</th>")
            print("<th class = \"grades-header\" >GRADE</th>")
            print("<th class = \"grades-header\" >Position</th>")
            
            agriculture = row[16]
            if(agriculture is None):
                agriculture = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Agriculture</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + agriculture + "</td>")
            print("<td class= \"student-data\">"+ studentPosition + "</td>")
            print("</tr>")
            
            bibleKnowledge = row[17]
            if(bibleKnowledge is None):
                bibleKnowledge = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Bible Knowledge</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + bibleKnowledge + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            biology = row[11]
            if(biology is None):
                biology = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Biology</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + biology + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            chemistry = row[10]
            if(chemistry is None):
                chemistry = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Chemistry</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + chemistry + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            chichewa = row[18]
            if(chichewa is None):
                chichewa = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Chichewa</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + chichewa + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            english = row[8]
            if(english is None):
                english = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">English</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + english + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            geography = row[15]
            if(geography is None):
                geography = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Geography</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + geography + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            history = row[14]
            if(history is None):
                history = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">History</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + history + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            maths = row[12]
            if(maths is None):
                maths = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Mathematics</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + maths + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            physics = row[9]
            if(physics is None):
                physics = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Physics</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + physics + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            socialStudies = row[13]
            if(socialStudies is None):
                socialStudies = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Social Studies</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + socialStudies + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
            print("</tr>")
            
            computerStudies = row[20]
            if(computerStudies is None):
                computerStudies = "&nbsp"
            print("<tr class= grades-section>")
            print("<th class= \"student-data\">Computer Studies</th>")
            print("<td class= \"student-data\">Mark</td>")
            print("<td class= \"student-data\">" + computerStudies + "</td>")
            print("<td class= \"student-data\">" + studentPosition + "</td>")
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
    cursor.close()    
print("Content-type: text/html")
print("")
print(open("all-printout.html").read())
displayPrinout()
