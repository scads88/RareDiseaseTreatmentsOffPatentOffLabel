# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:49:23 2018

@author: john3
"""


drug2diseasedic={}
for drug in druglist:
    if drug in treatmentlist[treatmentdescription]:
        drug2diseasedic[drug]=treatmentlist[diseasename]
        
        
        