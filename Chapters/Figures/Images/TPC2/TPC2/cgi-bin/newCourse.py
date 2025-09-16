#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> New Course </title>
</head>
<body> """)
    
form = cgi.FieldStorage()

id_num = str(form["code"].value)
first_name = str(form["course_name"].value)
students_enrolled = str(form["students_enrolled"].value)

db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()


try:
    cursor.execute('INSERT INTO courses VALUES( ?, ?, ?);' , \
               	( int(id_num), first_name, int(students_enrolled )))

				
except sqlite3.Error as er:
	print('Error in INSERT: ', er)
	raise Exception(print("""  <p> <a href="../index.html" > Return to main page. </a> </p>
</body>
</html>"""))


db_connection.commit()
db_connection.close()

print('<h2> A new course was added ' + \
	id_num +  ',' + first_name + '</h2> <p>')
print("""  <p> <a href="../index.html" > Return to main page. </a> </p>
</body>
</html>""")