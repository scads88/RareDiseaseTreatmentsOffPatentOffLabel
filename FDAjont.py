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



#webcrawler for nih raredisease website

#https://rarediseases.info.nih.gov/diseases/5748/adenosine-deaminase-deficiency
#https://rarediseases.info.nih.gov/diseases/5761/afibrinogenemia
#https://rarediseases.info.nih.gov/diseases/5622/cerebrotendinous-xanthomatosis
#https://rarediseases.info.nih.gov/diseases/5782/alopecia-areata
#https://rarediseases.info.nih.gov/diseases/5784/alpha-1-antitrypsin-deficiency

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
    print(poop[0])
#{k:v for k, v in zip(newnames, newlinks)}

