
# coding: utf-8

# In[15]:

langs = {}
import codecs
with codecs.open('input(5).txt', 'r', 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        line = line.split(' : ')
        langs[line[0]] = line[1]
        
        
n = int(input()) 
for i in range (n):
        s = input()
        for keys, t in langs.items():
            if s in t:
                print(keys, end = ' ')
        print(end = '\n')
        
        
    

