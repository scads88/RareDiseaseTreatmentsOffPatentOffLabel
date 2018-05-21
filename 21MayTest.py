# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:09:44 2018

@author: john3
"""

import csv
import pandas as pd
import numpy as np
import pickle
import glob





dfx=pd.read_csv("Treatment2Offlabel.csv", encoding="ISO-8859-1")
#print(dfx.head()["Ingredient"][2])

lengthofdfx=len(dfx.head())
for i in range(0, lengthofdfx):
    if "ACE" in dfx.head()["Ingredient"][i]:
        
        pass
        #print (dfx.head()["Ingredient"][i])

    

dfy=pd.read_csv("19MayTest3000_3250.csv", encoding="ISO-8859-1")  

    
#change short chain to treatment names and you good
druglist=[drug.lower() for drug in dfx["Ingredient"]]

#print(druglist)
specialword="treatment"

#druglist=["treatment", "limited", "carnitine"]
#print(druglist)
drug2treatmentdic={}
listofdrug2treatment=[]
lengthofdfy=len(dfy)
#print(lengthofdfy)




pussydic={}
    
print(druglist)
#print(dfy["Current Standard of Treatment if Listed on NIH Rare Diseases Website"].lower())
 
for i in range(0, lengthofdfy):      
    for drug in druglist:
        if drug in dfy["Current Standard of Treatment if Listed on NIH Rare Diseases Website"][i]:
            print (drug, "-", dfy["Disease Name"][i])
            pussydic[drug]=dfy["Disease Name"][i]
print(pussydic)

df=pd.DataFrame.from_dict(pussydic, orient="index")
print(df)
df.to_csv("ass.csv")




            
            
        #print (drug)
        #if drug in dfy["Current Standard of Treatment if Listed on NIH Rare Diseases Website"][i]:
            #print(dfy["Disease Name"][i])
            #print("dick")
#print (counter)
#for i in dfx.head()["Ingredient"]:
#    print (i)
    