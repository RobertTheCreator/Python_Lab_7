
# coding: utf-8

# In[61]:

import string
import codecs
enru = {}
with codecs.open('en-ru.txt', 'r', 'utf-8') as f:
    for line in f:
        line = line.strip('\n')
        a = list(line.split('\t-\t'))
        enru[a[0]] = a[1]

with open('input(4).txt', 'r') as q:
    output = open('output1.txt', 'w')
    for line in q:
        line = line.strip('\n')
        print(line)
        output.write(line)
        output.write('\n')
        for elem in string.punctuation:
            line1 = line.replace(elem, ' ')
        b = list(line1.split(' '))
        for key in b:
            if key in enru:
                line1 = line1.replace(key, enru[key])
            if key.lower() in enru:
                line1 = line1.replace(key, enru[key.lower()].title())
        print(line1)
        output.write(line1)
        output.write('\n')
    output.close()


