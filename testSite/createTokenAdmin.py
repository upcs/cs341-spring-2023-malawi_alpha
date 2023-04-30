#!/usr/bin/python3
import cgi
import connection


def addTeacherBoxes():
    cursor = connection.connect()
    sql = "SELECT * FROM TeacherTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    i = 1
    for row in result:
        print(f'<input type = "checkbox" name = "{row[0]}" value = "{row[0]}"/> {row[1]} {row[2]}')
        if i % 3 == 0:
            print("<br>\n")
        else:
            print("")
        i += 1
    cursor.close()

def firstHalf():
    print("""
<body>

        <div id="tokensheet-body-cc"><center>
            <form action = "generatedToken.py" method = "post">
                <h3><center>Admin Privileges</center></h3>
                <input type = "checkbox" name = "Admin" value = "on" /> Admin Token (Has access to all classes)<br>
                <h3><center>Class Privileges</center></h3>
                <input type = "checkbox" name = "classes" value = "1" /> Math 
                <input type = "checkbox" name = "classes" value = "2" /> Social Studies <br>
                <input type = "checkbox" name = "classes" value = "3" /> English
                <input type = "checkbox" name = "classes" value = "4" /> Physics
                <input type = "checkbox" name = "classes" value = "5" /> Chemistry <br>
                <input type = "checkbox" name = "classes" value = "6" /> Biology
                <input type = "checkbox" name = "classes" value = "7" /> History 
                <input type = "checkbox" name = "classes" value = "8" /> Geography
                <input type = "checkbox" name = "classes" value = "9" /> Agriculture <br>
                <input type = "checkbox" name = "classes" value = "10" /> Bible Knowledge 
                <input type = "checkbox" name = "classes" value = "11" /> Chichewa 
                <input type = "checkbox" name = "classes" value = "12" /> French <br>
                <input type = "checkbox" name = "classes" value = "13" /> Computer Studies
                <input type = "checkbox" name = "classes" value = "14" /> Life Skills <br>
                <h3 id="teachersBoxes"><center>Teachers</center></h3>
                """)

def secondHalf():
    print("""
                <br>
                <button type = "submit" name = "submit" /> Generate Token
                </form>
            </center>
        </div>
        <br>
        <br>
            </tbody>
        </table>
    </body>
""")


  
  
    

print("Content-type: text/html")
print("")
print(open('createTokenAdmin.html').read())
firstHalf()
addTeacherBoxes()
secondHalf()
