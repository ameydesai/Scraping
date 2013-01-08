import httplib2
from BeautifulSoup import BeautifulSoup
import sqlite3



#f=open("../data/india-citieshtml.html","r").read()
connection=sqlite3.connect("/home/amey/atomparsing/src/database/feed.db")
cursor=connection.cursor()
http=httplib2.Http('.cache')
response,content=http.request("http://en.wikipedia.org/wiki/List_of_cities_and_towns_in_India",headers={'User-Agent':'Crawler-Project'})
if (response.status/100<4):
    soup=BeautifulSoup(content)
    dataTable=soup.findAll('table',{'class':'wikitable sortable'})
    for table in dataTable:
	rows=table.findAll("tr")
        rows=rows[1:]
        for row in rows:
		cursor.execute('Insert into cities VALUES(?)',(row.find("td").text,))

connection.commit()
cursor.close() 	    	

