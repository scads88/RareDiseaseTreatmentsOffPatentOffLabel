
#OVERALL GOAL IS CREATING A DISEASE: URL DICTIONARY --> CSV FILE using pandas


import requests
import csv
import bs4 as bs
import pandas as pd
import pickle
import string
import numpy as np

#generates the letters list for later use
letters = list(string.ascii_uppercase)
letters.append("0-9")
print(letters)
#generates name and link lists for later use
bignamelist=[]
biglinklist=[]

#generates an initial soup get request by iterating through letter list in conjunction with base rare disease url
for symbol in letters:
    rarediseaseurl=requests.get("https://rarediseases.info.nih.gov/diseases/browse-by-first-letter/"+symbol) #runs through all the different urls
    soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")

#gives all url pieces as a list
    namelist=[]
    for link in soup.select("a"): #helps select the text from the "a" tags in soup
        namelist.append(link.text) #helps select the text from the "a" tags in soup
    endnamelistcut=len(namelist)-17  #mod for what names need removal in the front of the list
    namelist=namelist[171:endnamelistcut] #mod for what names need removal in the front of the list
    for name in namelist:
        bignamelist.append(name)
    
    
    linklist=[]
    for link in soup.find_all("a", href=True): #helps select the hyperlinks from "a href" tags in soup
        linklist.append(link.get("href")) #helps select the hyperlinks from "a href" tags in soup
    endlinklistcut=len(linklist)-16 #mod for what links need removal at end of the list
    linklist=linklist[171:endlinklistcut] #mod for what links need removal in the front of the list
    for link in linklist:
        biglinklist.append(link)
    
    #a counter cuz it takes a while to run through all letters in list
    print(symbol +" has completed")

#how to pull the actual disease names + plus some trash from a hrefs

allnames2alllinksdic={k:v for k, v in zip(bignamelist, biglinklist)} #combines name and url list into key value pairs dictionary
df=pd.DataFrame.from_dict(allnames2alllinksdic, orient="index") #generates a pandas datafrome from the dictionary created above

#Boring but essential reformating of the dataframe to make it clean and easy to use
df = df.reset_index() 
df.reset_index(drop=True)
df["Name"]=df["index"]
df["URLS"]=df[0]
del df["index"]
del df[0]
df.index = np.arange(1, len(df) + 1)

with open("18MayTest.pickle", "wb") as f:
    pickle.dump(df, f)
    f.close()
#INSERT A PICKLE TEST AND GENERATION FEATURE HERE

df.to_csv("18MayTest.csv") #generates a csv for name, url dataframe
print(df["URLS"].head())






