#!/usr/bin/python3
import cgi
import connection
data = cgi.FieldStorage()
print('Content-type: text/html\r')
print("")

if len(data.keys()) == 0:
    print("<script>alert('No name entered')</script>")
    print("<script>window.location = 'teacher_view.py'</script>")
    print("\r\n")
name = data.getvalue('search-text')
name = name.strip()
names = name.split(" ")
firstName = names[0]
lastName = names[1]
cursor = connection.connect()
sql = "SELECT StudentID FROM GradeTbl WHERE FirstName = '" + firstName + "' AND LastName = '" + lastName + "';"
cursor.execute(sql)
result = cursor.fetchone()
if (result == None):
    print("<script>alert('Student not found')</script>")
    print("<script>window.location = 'teacher_view.py'</script>")
    print("\r\n")
print("<script>window.location = 'teacher-edit.py?ID=" + str(result[0]) + "'</script>")
# print("<script>window.location = teacher-edit.py?ID= + result + </script>")