#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
token = form.getvalue('token-text')

if token == '12345':
    print('Location: http://10.12.116.141/validated.py\r\n')
    print('Status: 302 Found\r\n')
    print('Content-type: text/html\r')
    print("Cache-Control: no-cache, no-store, must-revalidate")
    print("Pragma: no-cache")
    print("Expires: 0")
    print("\r\n")
else:
    print('Location: http://10.12.116.141/teacher_view.py\r\n')
    print('Status: 302 Found\r\n')
    print('Content-type: text/html\r')
    print("Cache-Control: no-cache, no-store, must-revalidate")
    print("Pragma: no-cache")
    print("Expires: 0")
    print("\r\n")
