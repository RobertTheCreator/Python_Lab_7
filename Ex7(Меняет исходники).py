
# coding: utf-8

# In[7]:

import codecs

enru = {}
ruen = {}

with codecs.open('en-ru(7).txt', 'r', 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        line = line.split('\t-\t')
        enru[line[0]] = line[1]
with codecs.open('ru-en(7).txt', 'r', 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        line = line.split('\t-\t')
        ruen[line[0]] = line[1]
print(len(enru), len(ruen))    

#дополнение и обновление
for key, elem in enru.items():
    for elem1 in elem.split(','):
        if elem1 in ruen:
            ruen[elem1] += ',' + key
        else:
            ruen[elem1] = key
            
            
for key, elem in ruen.items():
    for elem1 in elem.split(','):
        if elem1 in enru:
            if key not in enru[elem1].split(','):
                enru[elem1] += ',' + key
        else:
            enru[elem1] = key
print(len(enru), len(ruen)) 


#Запись новых словарей        
outputen = open('en-ru(7).txt', 'w')
for key in sorted(enru):
    outputen.write(key + '-' + enru[key])
    outputen.write('\n')
outputen.close()

outputru = open('ru-en(7).txt', 'w')
for key in sorted(ruen):
    outputru.write(key + '-' + ruen[key])
    outputru.write('\n')
outputru.close()

