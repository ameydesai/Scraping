import sqlite3
import time

today=time.strftime("%A, %B %d, %Y")
connection=sqlite3.connect("/home/amey/atomparsing/src/database/feed.db")
cursor=connection.cursor()
#cursor.execute('INSERT INTO mytable VALUES(null, ?, ?)', (today, "This entry could be the first item on a To-Do List, or it could be a journal entry, or whatever you want."))
#cursor.execute('INSERT INTO mytable VALUES(null, ?, ?)', (today, "To-Do: Write an SQLite3 tutorial!"))
#connection.commit()
cursor.execute('SELECT count(*) FROM geekTable')
#allentries=cursor.fetchall()
#for x in allentries:
    #print "Item number: " + str(x[0]) + "  Date: " + x[1] + "  Entry: " + x[2]
print cursor.fetchall()
cursor.execute('SELECT * FROM geekTableTiming')
print cursor.fetchall()
cursor.close()

