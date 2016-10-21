
# coding: utf-8

# In[83]:

import string
A = {}
with open('LICENSE.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        for elem in string.punctuation:
            line = line.replace(elem, ' ')
        stroka = line.lower()
        slova = stroka.split(' ')
        for value in slova:
            if value not in A:
                A[value] = 1
            else:
                A[value] += 1
max = 0
for key in A:
    if A[key] > max and key != '':
        max = A[key]
for key in A:
    if A[key] == max:
        print(key, max)

