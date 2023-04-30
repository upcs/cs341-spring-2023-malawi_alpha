#!/usr/bin/python3
import cgi 
import connection

print("Content-type: text/html")
print("")
data = cgi.FieldStorage()
form = -1

if ('firstName' not in data.keys()) or ('lastName' not in data.keys()):
    print("<script>alert('Please fill out all name fields')</script>")
    print("<script>window.location = 'add-student.py'</script>")
    print("\r\n")
elif 'form' not in data.keys():
    form = 'NULL'
else: 
    form = data.getvalue('form')
    
if form != 'NULL':
    try:
        form = int(form)
    except ValueError:
        print("<script>alert('Invalid input in Form')</script>")
        print("<script>window.location = 'add-student.py'</script>")
        print("\r\n")

cursor = connection.connect()
firstName = data.getvalue('firstName')
lastName = data.getvalue('lastName')
firstName = str(firstName)
lastName = str(lastName)
query = "INSERT INTO GradeTbl (FirstName, LastName, Form) VALUES ('" + firstName + "', '" + lastName + "', " + form + ");"

try:
    cursor.execute(query)
    cursor.connection.commit()
    cursor.connection.rollback()
    cursor.close()
    print("<script>alert('Student Added')</script>")
    print("<script>window.location = 'teacher_view.py'</script>")
    print("\r\n")
except:
    cursor.close()
    print("<script>alert('Error, Student Not Added')</script>")
    print("<script>window.location = 'add-student.py'</script>")
    print("\r\n")
    