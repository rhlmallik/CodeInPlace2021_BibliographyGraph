# -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:21:28 2021

@author: rhlma
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:07:28 2021

@author: rhlma
"""

import os
import re

#
#def papers_more_than1_cit(dict_bib, paper_name):
#    
#    for keys in dict_bib:
#        print(len(dict_bib[keys][2]))



directory = os.getcwd()

if os.path.exists(directory):
    # Build index from files in the given directory

    dict_bib = {}          # index is empty to start
    paper_name = {}    # mapping of file names to article titles is empty to start

    filenames = []
    doc = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(filename))
            
  
#        with open(current_file) as f_in:
#            doc = (line.rstrip() for line in f_in) 
#            doc = list(line for line in doc if line) # Non-blank lines in a list
    for current_file in filenames:        
        f_in = open(current_file)
        doc = (line.rstrip() for line in f_in) 
        doc = list(line for line in doc if line) # Non-blank lines in a list
        f_in.close()


        for i in range(len(doc)):
            if i==0:
                paper_name.update({current_file:doc[i]})
            else:
                new_str = re.split(r'\"', doc[i])      
                if new_str[1] not in dict_bib.keys():
                    dict_bib.update({new_str[1]:[new_str[0], new_str[2],[current_file]]})
                else:
                    dict_bib[new_str[1]][2].append(current_file)


    for keys in dict_bib:
        print(len(dict_bib[keys][2]))
















