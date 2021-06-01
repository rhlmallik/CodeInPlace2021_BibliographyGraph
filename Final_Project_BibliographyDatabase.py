# -*- coding: utf-8 -*-
"""
Created on Sat May 29 22:10:13 2021
This file is used to parse out the content of each text file.
Debugs: If bibliogrpahy references the books, it often fails to add "" marks and hence this 
code fails We have to first run this file to clean that up, manually
edit the files to add " when seemed needed.
@author: rhlma
"""
import re

dict_bib = {}
papername = {}

filename = "Brian_TPEL_13.txt" #"Minghui_ECCE_19.txt"  #"Marcello_ITAC_19.txt" #Hui_TPEL_20.txt"   #"Brian_TPEL_13.txt"
#with open(filename) as f_in:
#    doc = (line.rstrip() for line in f_in) 
#    doc = list(line for line in doc if line) # Non-blank lines in a list
    
f_in = open(filename)
doc = (line.rstrip() for line in f_in) 
doc = list(line for line in doc if line) # Non-blank lines in a list
f_in.close()

for i in range(len(doc)):
    if i==0:
        papername.update({filename:doc[i]})
    else:
        new_str = re.split(r'\"', doc[i])       
        dict_bib.update({new_str[0]:[filename,new_str[1],new_str[2]]})
        print(i)

        
#with open("Brian_TPEL_16.txt") as search:
#    next(search)
#    next(search)
#    for line in search:
#        lines = list(line for line in (strip() for l in f_in) if line)
#        line = line.strip()  # remove '\n' at end of line
#        new_str = re.split(r'\"', line)
##        dict_bib.update( {new_str[1] : new_str[0]} )
#        print(new_str )