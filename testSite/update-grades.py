#!/usr/bin/python3
import cgi
import connection
import os

dataset = cgi.FieldStorage()
id_value = dataset.getvalue('ID')
cursor = connection.connect()
sql = "SELECT * FROM GradeTbl WHERE StudentID = " + id_value
cursor.execute(sql)
result = cursor.fetchall()
queryResults = cursor.rowcount
col_names = [desc[0] for desc in cursor.description]

keys = dataset.keys()



url = 'http://10.12.116.141/teacher-edit.py?ID=' + id_value + "'"
print('Location: ' + url + '\r\n')
print('Status: 302 Found\r\n')
print('Content-type: text/html\r')
# print("Cache-Control: no-cache, no-store, must-revalidate")
# print("Pragma: no-cache")
# print("Expires: 0")
print("\r\n")


# form = cgi.FieldStorage()
# token = form.getvalue('token-text')
# # 5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5

# if token == '12345':
#     hash = hashlib.sha256(token.encode('utf-8'))
#     url = 'http://10.12.116.141/validated.py?ID=' + hash.hexdigest()
#     print('Location: ' + url + '\r\n')
#     print('Status: 302 Found\r\n')
#     print('Content-type: text/html\r')
#     print("Cache-Control: no-cache, no-store, must-revalidate")
#     print("Pragma: no-cache")
#     print("Expires: 0")
#     print("\r\n")
# else:
#     print('Location: http://10.12.116.141/teacher_view.py\r\n')
#     print('Status: 302 Found\r\n')
#     print('Content-type: text/html\r')
#     print("Cache-Control: no-cache, no-store, must-revalidate")
#     print("Pragma: no-cache")
#     print("Expires: 0")
#     print("\r\n")
