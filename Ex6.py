
# coding: utf-8

# In[66]:

words = {}
with open('en-ru(6).txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        line = line.split(' - ')
        words[line[0]] = line[1]
        
ruen = {}
for key, elem in words.items():
    for elem1 in elem.split(', '):
        if elem1 in ruen:
            ruen[elem1] += ', ' + key
        else:
            ruen[elem1] = key           

        
output = open('ru-en.txt', 'w')
for key in sorted(ruen):
    output.write(key + '-' + ruen[key])
    output.write('\n')
output.close()

