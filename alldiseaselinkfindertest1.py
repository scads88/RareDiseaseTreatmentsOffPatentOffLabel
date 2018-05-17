# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:53:43 2018

@author: john3
"""
import bs4 as bs
import csv

import requests

rarediseaseurl=requests.get("https://rarediseases.info.nih.gov/diseases/browse-by-first-letter/C")
soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")

#gives all url pieces as a list
dipshitlinks=[]
for link in soup.find_all("a", href=True):
    dipshitlinks.append(link.get("href"))
del dipshitlinks[-16:]
newlinks=dipshitlinks[171:]
#print(newlinks)
#print (len(newlinks))



#how to pull the actual disease names + plus some trash from a hrefs
names=[]  
for link in soup.select('a'):
    names.append(link.text)
del names[-17:]
newnames=names[171:]
#print(newnames)
#print (names)

newdic={k:v for k, v in zip(newnames, newlinks)}
print(newdic)

    
    



    


#print(poop)