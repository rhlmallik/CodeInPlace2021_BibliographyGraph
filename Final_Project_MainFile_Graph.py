# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:08:22 2021

Broad Overview:
In this code we try to select 6 papers and then we generate 6 files, one for each 
of the paper. These .txt files have been downloaded from the "References" section
of these papers in their IEEE page.
We then create a dictionary from those 6 .txt files in such a way that the dictionary title 
dict_bib : maps the 'title of the paper' to the .txt file it appeared in. 
Thus this dictionary can tell us that which paper (key) has been cited by which of the 
six original papers that we started working with.
The structure of the dict_bib is:

dict_bib{Paper_title1:[Authors on Paper_title1, Date of publication and other imp details,
                       ['Brian_TPEL.txt',... other files that has cited Paper_Title1]],
        Paper_title2:[Authors on Paper_title2, Date of publication and other imp details,
                       ['Brian_TPEL.txt',... other files that has cited Paper_Title2]]
                       }

Now we create a new dictionary called dict_cite which is keep a tally of "who cited whom,
and how many times". This dictionary will be then used for plotting the bibliography
network graph. So we can threshold the minimum number of citations eg2.
(This last part of network graph was not possible to be done in this notebook, so 
I completed it in Spyder)


@author: rhlma
"""



# importing networkx 
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt


import os
import numpy as np
import re
def create_dicts(filenames, dict_bib, paper_name):

    """
    This function takes in the bibliography files of the six original papers and
    gives the reverse index kind of function.
    The output :

    dict_bib : maps the paper titles found in the six .txt files to the specific .txt files
    which cited them, and also includes other necessary details

    paper_name : This stores the paper name of the six papers we start with. They are found 
    in the first line of each text file.

    paper_name: {'file.txt': Title on file.txt, 'file1.txt':Title on file1.txt,...}


    """    
    for current_file in filenames:
      
#        with open(current_file) as f_in:
#            doc = (line.rstrip() for line in f_in) 
#            doc = list(line for line in doc if line) # Non-blank lines in a list
            
        f_in = open(current_file)
        doc = (line.rstrip() for line in f_in) 
        doc = list(line for line in doc if line) # Non-blank lines in a list
        f_in.close()

        # usually references look like this :
        # 1. M. C. Chandorkar D. M. Divan and R. Adapa "Control of parallel 
        # connected inverters in standalone AC supply systems" IEEE Trans. Ind. 
        # Appl. vol. 29 no. 1 pp. 136-143 Jan. 1993.
        # We split the info by the \" character.
        # This gives us three parts,
        # The author names, the paper title, other details.
        # We want the paper title to be the key


        for i in range(len(doc)):
            if i==0:
                paper_name.update({current_file:doc[i].lower()})
            else:
                new_str = re.split(r'\"', doc[i])   
                if new_str[1].lower() not in dict_bib.keys():
                    dict_bib.update({new_str[1].lower():[new_str[0], new_str[2],[current_file]]})
                else:
                    dict_bib[new_str[1].lower()][2].append(current_file)
        



def textfiles_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a valid directory, returns a list of the .txt
    file names within it.

    Input:
        directory (string): name of directory
    Returns:
        list of (string) names of .txt files in directory
    """
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(filename))

    return filenames

def papers_more_thanN_cit(dict_bib, paper_name, dict_cite, threshold):

    """
    In this code we accept the output of the function create_dicts()
    And now we want to find which papers were references how many times and by whom.
    dict_cite = {'Title of paper':[[file1.txt,file2.txt.. whichever .txt file it appears in],
                                    number of .txt files it appears in (citation)]}
    """    
  
    for keys in dict_bib:
        citation = len(dict_bib[keys][2])
        if citation>= threshold:
            dict_cite.update({keys:[dict_bib[keys][2],citation]})

def plot_graph(dict_cite, paper_name):

    plt.figure(figsize=(15, 8))
    g = nx.Graph()
     
    for keys in dict_cite:
        g.add_node(keys)
        
    for keys in paper_name:
        g.add_node(paper_name[keys])

    for keys_papers in paper_name:
        for keys_dict in dict_cite:
            for item in dict_cite[keys_dict][0]:
                if item == keys_papers:
                    g.add_edge(keys_dict,paper_name[keys_papers])
                    
    node_color = [g.degree(v) for v in g]
    node_size = [1000*g.degree(v) for v in g]
    # node colour is a list of degrees of nodes
                          
    nx.draw_circular(g,
            with_labels=True, 
            node_size = node_size, 
            node_color = node_color,
            alpha = 0.7)
#    print(g.edges)
    plt.savefig("Bibliography.png", dpi=1000)
    plt.savefig("Bibliography.png")

#savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#        orientation='portrait', papertype=None, format=None,
#        transparent=False, bbox_inches=None, pad_inches=0.1,
#        frameon=None, metadata=None)

#    plt.plot(range(10))
#    plt.savefig('testplot.png')
#    Image.open('testplot.png').save('testplot.jpg','JPEG')
#def plot_graph(dict_cite, paper_name):
#    g = nx.Graph()
#     
#    for keys in dict_cite:
#        g.add_node(keys)
#        
#    for keys in paper_name:
#        g.add_node(keys)
#
#    for keys_papers in paper_name:
#        for keys_dict in dict_cite:
#            for item in dict_cite[keys_dict][0]:
#                if item == keys_papers:
#                    g.add_edge(keys_dict,keys_papers)
#                    
#    nx.draw(g)
#    print(g.edges)

def main():
    
    directory = os.getcwd()
    
    N_files  = int(input("Enter number of files you want to read, (max : 6)"))
    
    if os.path.exists(directory):
        # Build index from files in the given directory
        files = textfiles_in_dir(directory)
        
        for i in range(len(files)-N_files):
            files.pop()
        print(files)

        dict_bib = {}          # index is empty to start
        paper_name = {}    # mapping of file names to article titles is empty to start
        dict_cite = {}
        
        create_dicts(files, dict_bib, paper_name)
        
        # FInd how many minimum citations do you want to show in the graph
        threshold = 2        
        #make new dictionary with entries with more than threshold citation
        papers_more_thanN_cit(dict_bib, paper_name, dict_cite, threshold)
        
        plot_graph(dict_cite, paper_name)
        
 

if __name__ == '__main__':
    main()
    