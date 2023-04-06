#!/usr/bin/python3
from art import *
import pymysql
import cgi
import cgitb
import hashlib
import sys

# cgitb.enable()  

# Art=text2art("AUTHEN",font='block',chr_ignore=True)
# print('Content-Type: text/plain')
# print('')
# print('Python Script Test Page!')
# print(Art)

# hash password 
#x = hashlib.new('ripemd160')
#x.update(b"12345")
#print(x.digest().hex())

conn = pymysql.connect(
    db='MalawiDB',
    user='root',
    passwd='cs341mwalpha',
    host='localhost')
c = conn.cursor()

# Gets form value
data = cgi.FieldStorage()
tokenEntered = data.getvalue('token')

str = hashlib.sha256(tokenEntered.encode('utf-8'))
token_hashed = str.hexdigest()
# print(token_hashed)

# Print the contents of the database.
sql = 'SELECT * FROM TokenTbl WHERE Token= %s'
c.execute(sql, token_hashed)
totalTokens = c.fetchall()
## only executes if one of those tokens axist
if len(totalTokens) == 1:
	## checks to see if tokentype in the database is teacher or admin
	if (totalTokens[0][2] == 'teacher'):
		print('Location: http://10.12.116.141/teacher_view.py\r\n')
		print('Status: 302 Found\r\n')
		print('Content-type: text/html\r')
		print("\r\n")
		

	elif (totalTokens[0][2] == 'admin'):
		print('Location: http://10.12.116.141/adminPage.py\r\n')
		print('Status: 302 Found\r\n')
		print('Content-type: text/html\r')
		print("\r\n")
else:
	print("Content-type: text/html\r")
	print("Location: http://python.org/\r\n\r")	
	c.close()
