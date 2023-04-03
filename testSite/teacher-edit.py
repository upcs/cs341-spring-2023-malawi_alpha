#!/usr/bin/python3
import connection
import os


def printGrades():

    # get the ID from the query string
    query_string = os.environ.get('QUERY_STRING', '')
    params = query_string.split('&')
    id_value = None
    for param in params:
        name, value = param.split('=')
        if name == 'ID':
            id_value = value
            break

    cursor = connection.connect()
    sql = "SELECT * FROM GradeTbl WHERE StudentID = " + id_value
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    
    if(queryResults > 0):
        
        # Create dictionary of column names``
        col_names = [desc[0] for desc in cursor.description]
        
        
        for row in result:
            print("<h3 name='name-section'>" , row[col_names.index("FirstName")] , " " , row[col_names.index("LastName")] , "'s grades</h3>")
            print("<table>")
            for c_name in col_names:
                if c_name == 'StudentID' or c_name == 'FirstName' or c_name == 'LastName':
                    continue
                
                data = row[col_names.index(c_name)]
                if data == None:
                    data = "&nbsp;"
                print("<tr>")
                print("<td>", c_name, "</td>")
                print("<td>", data , "</td>")
                print("</tr>")
                
                
    print("<table>")
    
    
    
    

print("Content-type: text/html")
print("")
print(open('teacher-edit.html').read())
printGrades()
