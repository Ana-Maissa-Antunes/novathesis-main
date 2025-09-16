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
    <title> Change Students Number </title>
</head>
<body> """)
    
form = cgi.FieldStorage()

id_num = str(form["code"].value)
num = str(form["students_enrolled"].value)

db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()

cursor.execute('Select * from courses where course_id =?;', \
           	( int(id_num),))
                
result = cursor.fetchone()

if(not(result)):
    raise Exception(print('<h2> Course ' + id_num + ' does not exist. ' + '</h2><hr>' + ("""  <p> <a href="../index.html" > Return to main page. </a> </p>
</body>
</html>"""))) 

try:
    cursor.execute('UPDATE courses  SET students_enrolled = ? WHERE course_id = ? ;' , \
               	(int(num), int(id_num)))
except sqlite3.Error as er:
	print('Error in UPDATE: ', er)

db_connection.commit()
db_connection.close()

print('<h2> Course ' + \
	id_num +  ': number of students enrolled was set to ' + num + '</h2> <p>')
print("""  <p> <a href="../index.html" > Return to main page. </a> </p>
</body>
</html>""")