#!/usr/bin/python3

print('Content-type: text/html\r')
print("")
print("<title>Remove Student</title>")
print("<h1>Remove Student</h1>")

print("<form method=\"post\" action=\"student-removed.py\" class=\"table-form\">")
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
print("</table>")
print("<tr>")
print("<button style=\"float: center\" type=\"submit\" id=\"remove-button\">Remove Student</button >")
print("<tr>")
print("</form>")