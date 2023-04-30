#!/usr/bin/python3

print('Content-type: text/html\r')
print("")
print("<title>Add Student</title>")
print("<h1>Add Student</h1>")

print("<form method=\"post\" action=\"student-added.py\" class=\"table-form\">")
print("<table width=100%>")
print("<tr>")
print("<th>First Name</th>")
print("<td><textarea style=\"resize: none\" name=\"" + "firstName" +
                      "\" id=\"" + "firstName" + "\" cols=\"30\" rows=\"1\"></textarea></td>")
print("</tr>")
print("<tr>")
print("<th>Last Name</th>")
print("<td><textarea style=\"resize: none\" name=\"" + "lastName" +
                      "\" id=\"" + "lastName" + "\" cols=\"30\" rows=\"1\"></textarea></td>")
print("</tr>")

print("<tr>")
print("<th>Form</th>")
print("<td><textarea style=\"resize: none\" name=\"" + "form" +
                      "\" id=\"form\" cols=\"30\" rows=\"1\"></textarea></td>")
print("</tr>")
print("</table>")
print("<tr>")
print("<button style=\"float: center\" type=\"submit\" id=\"add-button\">Add Student</button >")
print("<tr>")
print("</form>")