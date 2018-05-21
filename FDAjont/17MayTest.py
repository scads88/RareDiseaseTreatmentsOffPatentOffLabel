# -*- coding: utf-8 -*-
"""
Created on Thu May 17 15:35:29 2018

@author: john3
"""

#prototype of 18MayTest
import requests
import csv
import bs4 as bs
import pandas as pd
import pickle
import string

letters = list(string.ascii_uppercase)
letters.append("0-9")
print(letters)
for symbol in letters:
    
    rarediseaseurl=requests.get("https://rarediseases.info.nih.gov/diseases/browse-by-first-letter/"+symbol)
    soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")

#gives all url pieces as a list
    totallinks=[]
    for link in soup.find_all("a", href=True):
        totallinks.append(link.get("href"))
    del totallinks[-16:]
    diseaselinks=totallinks[171:]


#how to pull the actual disease names + plus some trash from a hrefs
    names=[]  
    for link in soup.select('a'):
        names.append(link.text)
    del names[-17:]
    newnames=names[171:]
    print(symbol+" is done processing")
#print(newnames)
#print (names)

#this currently overwrites the previous letter and 
newdic={k:v for k, v in zip(newnames, diseaselinks)}
    
    



df=pd.DataFrame.from_dict(newdic)# dictionary turned into a pandas dataframe

with open("17MayTest2pickle", "wb") as f:
    pickle.dump(df, f)
    f.close()

#putpicklehere
df.to_csv("17MayTest2.csv")
print(df)






rarediseaseurl=requests.get("https://rarediseases.info.nih.gov/diseases/5622/cerebrotendinous-xanthomatosis")
soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")
diseasename=soup.find("h1").get_text()
butt=soup.find("div", {"id":"readSpeaker_diseaseTreatmentSection"})

diseaselist=[]
nameNtreatmentdic={}
if butt is None:
    print ("there is most likely no treatment section for this disease")
    exit
else:
    poop=[e.get_text(strip=True) for e in butt.select(".disease_answer")]
    #print(poop[0])
    {k:v for k, v in zip(newnames, newlinks)}