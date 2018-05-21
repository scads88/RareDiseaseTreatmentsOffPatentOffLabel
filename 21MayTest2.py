# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:32:28 2018

@author: john3
"""

import csv
import itertools as IT

filenames = ['1.csv', '2.csv']
handles = [open(filename, 'rb') for filename in filenames]    
readers = [csv.reader(f, delimiter=',') for f in handles]

with  open('combined.csv', 'wb') as h:
    writer = csv.writer(h, delimiter=',', lineterminator='\n', )
    for rows in IT.izip_longest(*readers, fillvalue=['']*2):
        combined_row = []
        for row in rows:
            row = row[:2] # select the columns you want
            if len(row) == 2:
                combined_row.extend(row)
            else:
                combined.extend(['']*2)
        writer.writerow(combined_row)

for f in handles:
    f.close()