import sqlite3
import httplib2
from BeautifulSoup import BeautifulSoup,SoupStrainer
import urllib2

connection=sqlite3.connect("/home/amey/atomparsing/src/database/feed.db")
cursor=connection.cursor()
cursor.execute("Select Link,CompanyURL,RootLocation from geektable where (CompanyURL<>'No URL' and Address='')")
entries=cursor.fetchall()
jobInformation={}
allUrls=[]
visitedUrls=[]
ignoreUrls=["facebook.com","twitter.com","google.com","yahoo.com",".asx",".bmp",".css",".doc",".docx",".flv",".gif",".jpeg","mailto:",".jpg",".mid",".mov",".mp3",".ogg",".pdf",".png",".ppt",".ra",".ram",".rm",".swf",".txt",".wav",".wma",".wmv",".xml",".zip",".m4a",".m4v",".mov",".mp4",".m4b",".rar",".exe",".dll",".js",".xls",".xlsx"]


def addUrlToSeed(link,url):
    if "http" in link["href"]:
        cursor.execute('Insert into url VALUES(?)',(link["href"],))
	allUrls.append(link["href"])
    else:
        if url[-1]=="/" and link['href'][0]=="/":
            cursor.execute('Insert into url VALUES(?)',(url+link['href'][1:],))
	    allUrls.append(url+link['href'][1:])
        else:
	    if not (url[-1] =="/" or link['href'][0] =="/"):
	        cursor.execute('Insert into url VALUES(?)',(url+"/"+link['href'],))
 	        allUrls.append(url+"/"+link['href'])
            else:
		cursor.execute('Insert into url VALUES(?)',(url+link['href'],))
		allUrls.append(url+link['href'])
    connection.commit() 



''' 
for entry in entries:
    allUrls.append(entry[1])
counter=0

allUrls=allUrls[1:100] 
for url in allUrls:
    if url not in visitedUrls:
	visitedUrls.append(url)
        http=httplib2.Http('.cache')
        try:
            response,content=http.request(url,headers={'User-Agent':'Crawler-Project'})        
            if (response.status/100<4):
                soup=BeautifulSoup(content)
                links=soup.findAll('a',href=True)
                for link in links:
                    if link.has_key('href'):
                        if len(link['href']) > 1:
                            if not any(x in link['href'] for x in ignoreUrls):
                                if link['href'][0]!="#":
				    addUrlToSeed(link,url)

        except Exception, e:
            cursor.execute("Insert into error Values(?)",(str(e)+str(url),))
            connection.commit()
            continue
 
'''   
cursor.close()
