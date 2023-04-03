#!/usr/bin/python3
import cgi
import connection 

def displayPrintout():
    print("Hello world")
           
print("Content-type: text/html")
print("")
print(open('single-printout.html').read())
displayPrintout()



