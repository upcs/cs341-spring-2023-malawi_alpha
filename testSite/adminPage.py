#!/usr/bin/python3
import cgi
import connection 

def printTable():
    
    cursor = connection.connect()
    sql = "SELECT * FROM TokenTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
   
    
    print("<table width=100%>")
    if(queryResults > 0):
        
        col_names = [desc[0] for desc in cursor.description]
        index = [0, 1, 2]
        tokenID = -1
        token = -1
        userType = -1 
        
        print("<tr>")
        
        print("<th>" + "TokenID" + "</th>")      
        print("<th>" + "Classes" + "</th>")      
        print("<th>" + "Teachers Currently Using" + "</th>")
            
        for row in result:
            teacherID = 0
            print("<tr>")
            for i in range(3):		## Token ID Column
                cursor2 = connection.connect()
                sql2 = "SELECT * FROM TokenPermTbl WHERE TokenID = " + str(row[0])
                cursor2.execute(sql2)
                result2 = cursor2.fetchall()
                queryResults2 = cursor2.rowcount

                if (i == 0):
                    print("<td>" , row[0] , "</td>")
                elif (i == 1):	## Classes Column
                    cursor4 = connection.connect()
                    classNames = []
                    for row2 in result2:		## Searches for class name based on classID
                        sql4 = "SELECT ClassName FROM ClassTbl WHERE ClassID = " + str(row2[1])
                        cursor4.execute(sql4) 
                        result4 = cursor4.fetchall()
                        classNames.append(result4[0][0])
                        teacherID = row2[2]

                    print("<td>")
                    print("<ul>")
                    for name in classNames:	## Searches through tokenpermtbl to see what classes it has access to
                        print("<li>" + str(name) + "</li>")
                    print("</ul>")
                    print("</td>")
                elif (i == 2):
                    cursor3 = connection.connect()
                    sql3 = "SELECT * FROM TeacherTbl WHERE TeacherID = " + str(teacherID) 
                    cursor3.execute(sql3)
                    result3 = cursor3.fetchall()
                    queryResults3 = cursor3.rowcount
                    for row3 in result3:
                         print("<td>" + str(row3[1]) + " " + str(row3[2]) + "</td>")
            print("</tr>")
        print("</tr>")    
    print("</table>")
    cursor.close()
    cursor2.close()
    cursor3.close()
    cursor4.close()
    
print("Content-type: text/html")
print("")
print(open('adminPage.html').read())
printTable()

