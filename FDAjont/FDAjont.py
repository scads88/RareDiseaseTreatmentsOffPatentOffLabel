# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:06:02 2018

@author: john3
"""

import csv
import glob
import requests
import bs4 as bs


filename=glob.glob("*.csv")


#makes an empty list drugnames which will be populated with the csv
drugnames=[]

#extracts information from the pdf --> csv formatted table from the fda
for box in csv.reader(open(filename[0])):
    
    #adds the names of the drugs from the first column to the"drugnames" list
    drugnames.append(box[0])


#searches all drug names in FDA Offpatent Offlabel list
#will eventually use this a matchlist

"""
searchterm="AMINO"
for drug in drugnames:
    if searchterm in drug:
        print (drug)
        """


#webcrawler for nih raredisease website
crawlterm="#diseaseTreatmentSection"
crawllist=[]
#https://rarediseases.info.nih.gov/diseases/5748/adenosine-deaminase-deficiency
#https://rarediseases.info.nih.gov/diseases/5761/afibrinogenemia
#https://rarediseases.info.nih.gov/diseases/5622/cerebrotendinous-xanthomatosis
#https://rarediseases.info.nih.gov/diseases/5782/alopecia-areata
#https://rarediseases.info.nih.gov/diseases/5784/alpha-1-antitrypsin-deficiency
rarediseaseurl=requests.get("https://rarediseases.info.nih.gov/diseases/5622/cerebrotendinous-xanthomatosis")
soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")
butt=soup.find("div", {"id":"readSpeaker_diseaseTreatmentSection"})


if butt is None:
    print ("there is most likely no treatment section for this disease")
    exit
else:
    poop=[e.get_text(strip=True) for e in butt.select(".disease_answer")]
    print(poop[0])
    print(type(poop[0]))

#poop=[e.get_text(strip=True) for e in soup.select(".disease_answer")]


