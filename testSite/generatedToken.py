#!/usr/bin/python3
import cgi
import connection
import hashlib
import random
import string



def getValues():
    data = cgi.FieldStorage()

    cursor = connection.connect()
    sql = "SELECT * FROM ClassTbl"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount

    # choose from all lowercase letter
    letters = string.digits
    stringLength = 5
    randomToken = ''.join(random.choice(letters) for i in range(stringLength))
    str = hashlib.sha256(randomToken.encode('utf-8'))
    hashedKey = str.hexdigest()

    if (data.getvalue("Admin")):
        adminVal = True
    else:
        adminVal = False

    ## Gets values of classes that are checked
    classes = data.getlist("classes")
    cursor.close()
    cursor2 = connection.connect()

    sql2 = ""
    if adminVal:
        sql2 = "INSERT INTO TokenTbl VALUES (NULL, '" + hashedKey + "', 'admin');"
    else:
        sql2 = "INSERT INTO TokenTbl VALUES (NULL, '" + hashedKey + "', 'teacher');"

    try:
        cursor2.execute(sql2)
        cursor2.connection.commit()
        cursor2.connection.rollback()
        cursor2.close()
    except:
        cursor2.close()
        print("<script>alert('Error, Token Not Created')</script>")
        print("<script>window.location = 'adminPage.py'</script>")
        print("\r\n")

    cursor3 = connection.connect()
    sql3 = "SELECT TokenID FROM TokenTbl ORDER BY TokenID DESC LIMIT 1;"
    cursor3.execute(sql3)
    result3 = cursor3.fetchall()
    for row in result3:
        newestID = row[0]
    cursor3.close()

    ## BUGS
    # cursor4 = connection.connect()
    # for classID in classes:
    #     sql4 = "INSERT INTO TokenPermTbl VALUES ('" + newestID +"', '" + classID + "', '1');"
    #     print(sql4)
    #     #cursor4.execute(sql4)

    print("<script>alert('Token Added') Remember the token:" + randomToken + "</script>")
    print("<script>window.location = 'adminPage.py'</script>")
    print("\r\n")
    cursor4.close()
        


print("Content-type: text/html")
print("")
print(open('adminPage.html').read())
getValues()
