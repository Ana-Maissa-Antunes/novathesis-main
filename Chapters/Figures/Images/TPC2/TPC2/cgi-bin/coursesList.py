#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!
import sqlite3
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> Courses </title>
</head>
<body>
    <h1> Course List </h1>""")

db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()
try:
    cursor.execute("SELECT * FROM courses;")
    linhas = cursor.fetchall()
except sqlite3.Error as er:
	print('Error in SELECT:', er)
    

coursesNumber=0
studentsNumber = 0
for linha in linhas:
    print( '<li>' + str(linha[0]) + ' ' + str(linha[1]) + ' ' \
          + str(linha[2]), '</li>')
    coursesNumber += 1
    studentsNumber += linha[2]

if(not(coursesNumber)):
    raise Exception(print('<h2> Course List is empty.' + '</h2><hr>'+ ("""  <p> <a href="../index.html" > Return to main page. </a> </p>
</body>
</html>"""))) 

studentsNumberAvg = studentsNumber/coursesNumber

print('<p><hr> Number of courses = ' + str(coursesNumber) \
      + ' Total number of students = ' + str(studentsNumber) \
      + ' Average number of students = ' + str(studentsNumberAvg) + '<hr>')

print("""  <p> <a href="../index.html" > Return to main page. </a> </p>
</body>
</html>""")

db_connection.commit()
db_connection.close()

