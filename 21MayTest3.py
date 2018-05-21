# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:44:12 2018

@author: john3
"""
#precursor to 21maytest4 which is the final version thus far

import csv
import pandas as pd
import numpy as np
import pickle
import glob


dfx=pd.read_csv("Treatment2Offlabel.csv", encoding="ISO-8859-1")
druglist=[drug.lower() for drug in dfx["Ingredient"]]
druglist2=[drug.capitalize() for drug in dfx["Ingredient"]]
druglist=druglist+druglist2
drug2treatmentdic={}
listofdrug2treatment=[]

pussydic={}

letters = list(string.ascii_uppercase)

counter=0
filelist=glob.glob("DiseaseWtreatment_Description_Number/*.csv")
for file in filelist:
    try:
        dfy=pd.read_csv(file, encoding="ISO-8859-1")  
        lengthofdfy=len(dfy)
        
        for i in range(0, lengthofdfy):      
            for drug in druglist:
                if drug in dfy["Current Standard of Treatment if Listed on NIH Rare Diseases Website"][i]:
                    print (counter,drug, "-", dfy["Disease Name"][i])
                    #pussydic[drug+str(counter)]=dfy["Disease Name"][i]
                    pussydic[dfy["Disease Name"][i]+"-"str(counter)]=drug
                    counter=counter+1
    except KeyError:
        pass
print(pussydic)

df=pd.DataFrame.from_dict(pussydic, orient="index")
df.to_csv("OPOLT4D_XXXX.csv")

