#!/usr/bin/python3
import cgi
import connection


def printTable(page, rows_per_page):

    # Calculate the range of rows to fetch
    start_row = (page - 1) * rows_per_page
    end_row = start_row + rows_per_page
    
    cursor = connection.connect()
    sql = f"SELECT * FROM GradeTbl LIMIT {start_row}, {rows_per_page}"
    cursor.execute(sql)
    result = cursor.fetchall()
    queryResults = cursor.rowcount
    
    
    print("<form method=\"post\" action=\"test-update.py\" class=\"table-form\">")
    print("<button type=\"submit\" id=\"update-grade-button\" action=\"update-grades.py\">Update Grades</button >")
    print("<table width=100%>")
    if (queryResults > 0):

        col_names = [desc[0] for desc in cursor.description]
        currID = 1
        firstName = -1
        lastName = -1

        print("<tr>")
        for col in col_names:
            if col == "ClassID":
                continue
            if (col == "FirstName"):
                firstName = col_names.index(col)
                continue
            elif (col == "LastName"):
                lastName = col_names.index(col)
                print("<th class = 'rotate-text'> Name </th>")
                continue
            print("<th class = 'rotate-text'>" + col + "</th>")

        for row in result:
            print("<tr>")
            for col in col_names:
                if col == "ClassID":
                    continue
                if (col == "FirstName"):
                    continue
                elif (col == "LastName"):
                    print("<th><a href=teacher-edit.py?ID=" +
                          str(row[currID]) + ">", row[firstName], " ", row[lastName] + "</a></th>")
                    continue
                data = str(row[col_names.index(col)])
                if (data != "None"):
                    print("<td><textarea class=\"grade-edit-box\" name=\"" + col +
                      "\" id=\"" + col + "\" cols=\"30\" rows=\"1\">",data,"</textarea></td>")
                else:
                    print("<td><textarea class=\"grade-edit-box\" name=\"" + col +
                      "\" id=\"" + col + "\" cols=\"30\" rows=\"1\">.</textarea></td>")
            print("</tr>")
        print("</tr>")

    print("</table>")
    print("</form >")
    
    cursor.close()

def print_pagination_buttons(page, total_rows, rows_per_page):
    print('<div class="pagination-buttons">')
    total_pages = (total_rows + rows_per_page - 1) // rows_per_page
    
    if page > 1:
        print(f'<a href="?page={page - 1}">&lt; Previous</a>')

    for i in range(1, total_pages + 1):
        if i == page:
            print(f'<strong>{i}</strong>')
        else:
            print(f'<a href="?page={i}">{i}</a>')

    if page < total_pages:
        print(f'<a href="?page={page + 1}">Next &gt;</a>')
    print('</div>')

def get_total_rows():
    cursor = connection.connect()
    cursor.execute("SELECT COUNT(*) FROM GradeTbl")
    total_rows = cursor.fetchone()[0]
    cursor.close()
    return total_rows
    

form = cgi.FieldStorage()
page = int(form.getvalue("page", 1))  
rows_per_page = 25

print("Content-type: text/html")
print("")
print(open('update-view.html').read())

total_rows = get_total_rows()
print_pagination_buttons(page, total_rows, rows_per_page)
printTable(page, rows_per_page)

