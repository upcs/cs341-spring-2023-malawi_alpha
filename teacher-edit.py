#!/usr/bin/env python3

import cgi
import json
import mysql.connector
import os
import sys

#init the connection with the server... add your own credentials
def get_db_connection():
    return mysql.connector.connect(
        host="cs341mwalpha.campus.up.edu",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_database_name"
    )

#this function will get the grades for the selected class in the database
def get_grades(selected_class):
    grades = []

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = f"SELECT name, grade, behavior FROM students WHERE class = %s"
    cursor.execute(query, (selected_class,))

    for row in cursor.fetchall():
        grades.append(row)

    cursor.close()
    connection.close()

    return grades

if __name__ == '__main__':
    if 'REQUEST_METHOD' in os.environ and os.environ['REQUEST_METHOD'] == 'GET':
        form = cgi.FieldStorage()
        selected_class = form.getvalue("class")
        grades = get_grades(selected_class)

        sys.stdout.buffer.write(b"Content-Type: application/json\r\n")
        sys.stdout.buffer.write(b"\r\n")
        sys.stdout.buffer.write(json.dumps(grades).encode('utf-8'))
