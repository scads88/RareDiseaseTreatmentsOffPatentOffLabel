# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:26:45 2018

@author: john3
"""

import csv
import pandas as pd
import numpy as np
import pickle
import glob
import string
#reads in the program prepared Treatment2Offlabel.csv into pandas dataframe which contains off patent off exclusivity drugs from fda
dfx=pd.read_csv("Treatment2Offlabel.csv", encoding="ISO-8859-1")

#generates a list for the list of drugs found within. Nice job with streamlined for loops for lower and capitalization
druglist=[drug.lower() for drug in dfx["Ingredient"]]
druglist2=[drug.capitalize() for drug in dfx["Ingredient"]]
druglist=druglist+druglist2

drug2treatmentdic={}
listofdrug2treatment=[]
pussydic={}
letters = list(string.ascii_uppercase)
counter=0

#Accesses all .csv files in the DiseaseWtreatment_Description_Number Directory. These are the 250ish or so segments for all rare disease with treatment section. Generated by 19MayTest2
filelist=glob.glob("DiseaseWtreatment_Description_Number/*.csv")
for file in filelist:
    try:
        dfy=pd.read_csv(file, encoding="ISO-8859-1")  #files read into pandas dataframe
        lengthofdfy=len(dfy)
        
        for i in range(0, lengthofdfy):   #iterates through size of data frame   
            for drug in druglist: #iterates through druglist
                if drug in dfy["Current Standard of Treatment if Listed on NIH Rare Diseases Website"][i]: #asks if drug in disease treatment dataframe column
                    counter=counter+1
                    print (counter,drug, "-", dfy["Disease Name"][i])
                    #pussydic[drug+str(counter)]=dfy["Disease Name"][i]
                    pussydic[dfy["Disease Name"][i]+"^"+str(counter)]=drug #populates the dictionary that eventually will go on to make the disease:OPOEdrug file with
    except KeyError:
        pass
df=pd.DataFrame.from_dict(pussydic, orient="index") #turns dictionary into dataframe

#Boring but nice of the dataframe to make it clean and easy to use
df = df.reset_index() 
df.reset_index(drop=True)
df["Disease Name"]=df["index"]
df["Potential OPOE Treatment"]=df[0]
del df["index"]
del df[0]
df.index = np.arange(1, len(df) + 1)

df.to_csv("OPOLT4D_5.csv") #turns dataframe into .csv file