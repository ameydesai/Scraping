import urllib2
import re
import pickle
import sys
import time
import math
from BeautifulSoup import BeautifulSoup

#reviewsurl="http://mumbai.burrp.com/listing/grillopolis_andheri-west_mumbai_bars-pubs-restaurants-lounges/1975858712__UR__reviews?page="
f=open('1975858712__UR__reviews.htm','r').read()

reviewspagecounter=0
noofpages=1
reviewurls=[]
while True:
    #reviewreq=urllib2.Request(reviewsurl+str(reviewspagecounter))
    #reviewpage=urllib2.urlopen(reviewreq)
    
    if reviewspagecounter!=noofpages:    
	reviewspagecounter+=1	        
	reviewsoup=BeautifulSoup(f)
        totalreviews=float(re.findall(r'\d+',reviewsoup.find('a',{'class':'count'}).text)[0])
        if totalreviews is 0:
	    break
        reviewsperpage=float(re.findall(r'\d+',reviewsoup('a',{'href':'/listing/grillopolis_andheri-west_mumbai_bars-pubs-restaurants-lounges/1975858712__UR__reviews?page=2'})[1].text)[0])
	if reviewsperpage is 0:
	    break        
	noofpages=math.ceil(totalreviews/reviewsperpage)
        reviewtext=reviewsoup('div',{'style':'padding:0 0 3px;'})
        reviewrating=reviewsoup('span',{'class':'value-title'})
	reviewcomponent=reviewsoup('ul',{'class':'hreview estab_review'})
        for temp in reviewcomponent:
	    
	    if 'read more' in temp.text:
		readmoreurl=temp('a',{'class':'url'})		
		print readmoreurl[0]['href']
		print "\n"
		print "URL Request for read more kind of sections"
	   else:
		
	    
	#for temp in reviewtext:
		#print temp.text
		#print "\n"			
        #reviewurl=reviewsoup('li',{'class':'estab_reviewtext'})
        #for reviewlinks in reviewurl:
	    #href=reviewlinks('a',{'class':'url'})[0]['href']        
	    #reviewurls.append(href)
        
    else:
	break

    break
