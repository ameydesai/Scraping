import sqlite3
feedDB="/home/amey/atomparsing/src/database/feed.db"
connection=sqlite3.connect(feedDB)
cursor=connection.cursor()
#cursor.execute('CREATE TABLE mytable (Id INTEGER PRIMARY KEY, Date TEXT, Entry TEXT)')
#cursor.execute('Drop Table mytable')
#cursor.execute('CREATE TABLE geekTable(Link TEXT PRIMARY KEY, Name TEXT,CompanyURL TEXT,RootLocation TEXT,Address TEXT,JobTitle TEXT,JobSummary TEXT)')
#cursor.execute('CREATE TABLE geekTableTiming(LastUpdatedTime TEXT)')
#cursor.execute('Drop table geekTableTiming')
#cursor.execute('Delete from geekTableTiming where LastUpdatedTime="2012-05-20T02:24:56Z" ')
#cursor.execute('CREATE TABLE url(link TEXT)')
#cursor.execute('CREATE TABLE error(data TEXT)')
#cursor.execute("Create Table cities(Name Text)")
connection.commit()
cursor.close()


