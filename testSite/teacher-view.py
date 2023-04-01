#!/usr/bin/python3
import cgi
import connection 

def printTable():
    
    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    curr = 1
    print("<table width=100%>")
    if(queryResults > 0):
        print ("<tr>")
        print("<th class = 'rotate-text'>Class</th>")
        print( "<th class = 'rotate-text'>Name</th>")
        print( "<th class = 'rotate-text'>Position</th>")
        print( "<th class = 'rotate-text'>Best of Five plus Eng</th>")
        print( "<th class = 'rotate-text'>Running Average</th>")
        print( "<th class = 'rotate-text'>POINTS</th>")
        print( "<th class = 'rotate-text'>English</th>")
        print( "<th class = 'rotate-text'>Physics</th>")
        print( "<th class = 'rotate-text'>Chemistry</th>")
        print( "<th class = 'rotate-text'>Biology</th>")
        print( "<th class = 'rotate-text'>Maths</th>")
        print( "<th class = 'rotate-text'>Social Studies</th>")
        print( "<th class = 'rotate-text'>History</th>")
        print( "<th class = 'rotate-text'>Geography</th>")
        print( "<th class = 'rotate-text'>Agriculture</th>")
        print( "<th class = 'rotate-text'>Bible Knowledge</th>")
        print( "<th class = 'rotate-text'>Chichewa</th>")
        print( "<th class = 'rotate-text'>French</th>")
        print( "<th class = 'rotate-text'>Computer Studies</th>")
        print( "<th class = 'rotate-text'>Life Skills</th>")
        print( "</tr>")
        for row in result:
            print("<tr>")
            
            classID = row[1]
            if(classID is None):
                classID = "&nbsp"
            print("<td>" + classID + "</td>")
            
            #get values from table
            studentID = str(row[0])
            firstName = str(row[2])
            lastName = str(row[3])    
          
            # print("<th><a href='teacher-edit.py?ID='" + studentID + ">" + firstName + " " + lastName+ "</a></th>")
            print("<th><a href=teacher-edit.py?ID=" + studentID + ">" + firstName + " " + lastName+ "</a></th>")
            curr += 1
            
            studentPosition = row[4]
            if(studentPosition is None):
                studentPosition = "&nbsp"
            print("<td>" + studentPosition + "</td>")
            
            bofpe = row[5]
            if(bofpe is None):
                bofpe = "&nbsp"
            print("<td>" + bofpe + "</td>")
            
            running = row[6]
            if(running is None):
                running = "&nbsp"
            print("<td>" + running + "</td>")
            
            points = row[7]
            if(points is None):
                points = "&nbsp"
            print("<td>" + points + "</td>")
        
            english = row[8]
            if(english is None):
                english = "&nbsp"
            print("<td>" + english + "</td>")
            
            physics = row[9]
            if(physics is None):
                physics = "&nbsp"
            print("<td>" + physics + "</td>")
            
            chemistry = row[10]
            if(chemistry is None):
                chemistry = "&nbsp"
            print("<td>" + chemistry + "</td>")
            
            biology = row[11]
            if(biology is None):
                biology = "&nbsp"
            print("<td>" + biology + "</td>")
            
            maths = row[12]
            if(maths is None):
                maths = "&nbsp"
            print("<td>" + maths + "</td>")
            
            socialStudies = row[13]
            if(socialStudies is None):
                socialStudies = "&nbsp"
            print("<td>" + socialStudies + "</td>")
            
            history = row[14]
            if(history is None):
                history = "&nbsp"
            print("<td>" + history + "</td>")
            
            geography = row[15]
            if(geography is None):
                geography = "&nbsp"
            print("<td>" + geography + "</td>")
            
            agriculture = row[16]
            if(agriculture is None):
                agriculture = "&nbsp"
            print("<td>" + agriculture + "</td>")

            bibleKnowledge = row[17]
            if(bibleKnowledge is None):
                bibleKnowledge = "&nbsp"
            print("<td>" + bibleKnowledge + "</td>")
            
            chichewa = row[18]
            if(chichewa is None):
                chichewa = "&nbsp"
            print("<td>" + chichewa + "</td>")
            
            french = row[19]
            if(french is None):
                french = "&nbsp"
            print("<td>" + french + "</td>")
            
            computerStudies = row[20]
            if(computerStudies is None):
                computerStudies = "&nbsp"
            print("<td>" + computerStudies + "</td>")
            
            lifeSkills = row[21]
            if(lifeSkills is None):
                lifeSkills = "&nbsp"
            print("<td>" + lifeSkills + "</td>")
            
            print("</tr>")
    print("</table>")
    cursor.close()
    
print("Content-type: text/html")
print("")
print(open('teacher-view.html').read())
printTable()
