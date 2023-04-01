#!/usr/bin/python3
from art import *
import pymysql
import cgi
import cgitb
import hashlib

# cgitb.enable()  

Art=text2art("AUTHEN",font='block',chr_ignore=True)
print('Content-Type: text/plain')
print('')
print('Python Script Test Page!')
print(Art)
print("hello world!")

# hash password 
# x = hashlib.new('ripemd160')
# x.update(b"12345")
# print(x.digest().hex())

conn = pymysql.connect(
    db='MalawiDB',
    user='root',
    passwd='cs341mwalpha',
    host='localhost')
c = conn.cursor()

# Gets form value
data = cgi.FieldStorage()
tokenEntered = data.getvalue('token')


# Print the contents of the database.
c.execute(f'SELECT * FROM TokenTbl WHERE Token={tokenEntered}')
hashedToken = hash(tokenEntered)


# print(tokenEntered)
# print(hashedToken)
print([(r[2], r[3]) for r in c.fetchall()])
