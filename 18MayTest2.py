# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:47:33 2018

@author: john3
"""
import csv
import glob
import requests
import bs4 as bs
import pickle
import pandas as pd
import numpy as np

with open("18MayTest.pickle", "rb") as f:
    pickle.load(f)
    f.close()
print(df["URLS"].head(2))


for i in df["URLS"]:
    


    rarediseaseurl=requests.get("https://rarediseases.info.nih.gov"+i)
    soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")
    diseasename=soup.find("h1").get_text()
    print(diseasename)
    butt=soup.find("div", {"id":"readSpeaker_diseaseTreatmentSection"})
    diseaselist=[]
    nameNtreatmentdic={}
    if butt is None:
        print ("there is most likely no treatment section for this disease")
        exit
    else:
        try:
            poop=[e.get_text(strip=True) for e in butt.select(".disease_answer")]
            df["Treatment"]=poop
            print(poop[0])
        except:
            IndexError
            continue


df.to_csv("18MayTestAddTreatment.csv")