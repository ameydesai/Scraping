import feedparser
from datetime import datetime
from BeautifulSoup import BeautifulSoup
import sqlite3


#f=open("../data/feed.htm","r").read()
#hasGeekFeed=feedparser.parse('http://jobs.hasgeek.com/feed')
connection=sqlite3.connect("/home/amey/atomparsing/src/database/feed.db")
cursor=connection.cursor()
cursor.execute("Select LastUpdatedTime from geekTableTiming")

#lastUpdatedTime=datetime.strptime(list(cursor.fetchone())[0],'%Y-%m-%dT%H:%M:%SZ').isoformat()
#currentFeedTime=datetime.strptime(str(hasGeekFeed.feed.updated),'%Y-%m-%dT%H:%M:%SZ').isoformat()
cursor.execute("Select LOWER(NAME) from cities")
temp=cursor.fetchall()
cities=[]
for val in temp:
    cities.append(''.join(val).replace(",",""))
citiesFound=[]    


def loopOverCities(location):
    citiesForALoc=[]     
    for city in cities:
        if city in location:
	    if city not in citiesFound:
                citiesFound.append(city)
	    citiesForALoc.append(city)
    return citiesForALoc   

def loopOverCitiesFound(location):
    citiesForALoc=[]
    for city in citiesFound:
	if city in location:
	    citiesForALoc.append(city)
    return citiesForALoc	   


def checkLocationInExisitingCities(location):
    citiesForALoc=loopOverCities(location)
    citiesFoundForALoc=loopOverCitiesFound(location)
               
             

print checkLocationInExisitingCities("mUMBAI".lower())

'''
if currentFeedTime > lastUpdatedTime:
    cursor.execute('Delete from geekTableTiming')   
    cursor.execute('Insert into geekTableTiming (LastUpdatedTime) Values(?)',(hasGeekFeed.feed.updated,))

    keysToExtract=['id','summary','title']

    valuesForDb=[]
    link=[]
    for entry in hasGeekFeed.entries:
        newEntryStatus=True
        for k,v in entry.items():
            
            if k is 'updated':
               entryFeedTime=datetime.strptime(str(v),'%Y-%m-%dT%H:%M:%SZ').isoformat()
               if entryFeedTime <= lastUpdatedTime:
                   newEntryStatus=False
                   break
            if any(k in keys for keys in keysToExtract):
       	       if k is keysToExtract[1]:
	     
	          soup=BeautifulSoup(v)
                  companyInfoTags=soup.find('p')
                  companyLink=companyInfoTags.find('a')
              
                  if companyLink is not None:
                     valuesForDb.append(companyLink['href']) #2)URL
                     valuesForDb.append(companyLink.text)    #3)CompanyName
		  	
                  else:
		     valuesForDb.append("No URL")
                     valuesForDb.append(companyInfoTags.find('strong').text)
    
	          valuesForDb.append(soup.find('strong').nextSibling.nextSibling.strip()) #4)Location  
                  contentTags=soup.findAll('p')
             
                  contentText=[]
                  for tag in contentTags[1:]:
                      contentText.append(tag.text)
                  valuesForDb.append("".join(contentText))    	#5)Summary
       	       else:
                  valuesForDb.append(v) #1)Job Title 6)LinkID   
        
        if not newEntryStatus:
           break 
        cursor.execute('Insert into geekTable VALUES(?,?,?,?,?,?,?)',(valuesForDb[5],valuesForDb[2],valuesForDb[1],valuesForDb[3],"",valuesForDb[0],valuesForDb[4]))
    
        del valuesForDb[:]
'''
connection.commit() 
cursor.close()
	          






