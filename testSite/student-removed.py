#!/usr/bin/python3
import cgi 
import connection

print("Content-type: text/html")
print("")
data = cgi.FieldStorage()

if ('firstName' not in data.keys()) or ('lastName' not in data.keys()):
    print("<script>alert('Please fill out all name fields')</script>")
    print("<script>window.location = 'remove-student.py'</script>")
    print("\r\n")


cursor = connection.connect()
firstName = data.getvalue('firstName')
lastName = data.getvalue('lastName')
firstName = str(firstName)
lastName = str(lastName)
query = "DELETE FROM GradeTbl WHERE FirstName = '" + firstName + "' AND LastName = '" + lastName + "';"

check = "SELECT * FROM GradeTbl WHERE FirstName = '" + firstName + "' AND LastName = '" + lastName + "';"
cursor.execute(check)
if (cursor.rowcount <= 0):
    print("<script>alert('Student does not exist')</script>")
    print("<script>window.location = 'remove-student.py'</script>")
    print("\r\n")
    cursor.close()
    exit()
try:
    cursor.execute(query)
    cursor.connection.commit()
    cursor.connection.rollback()
    cursor.close()
    print("<script>alert('Student Removed')</script>")
    print("<script>window.location = 'teacher_view.py'</script>")
    print("\r\n")
except:
    cursor.close()
    print("<script>alert('Error, Student Not Removed')</script>")
    print("<script>window.location = 'remove-student.py'</script>")
    print("\r\n")
