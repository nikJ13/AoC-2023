# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:48:50 2023

@author: niket
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:35:38 2023

@author: niket
"""

def splitLine(text):
    return text.split('; ')

def updateCount(text):
    n = len(text)
    for i in range(n):
        text1 = text[i].split()
        if dict1[text1[1]]<=int(text1[0]):
            dict1[text1[1]] = int(text1[0])
    return

def checkAns():
    return dict1['red']*dict1['green']*dict1['blue']

dict1 = {'red':0,'green':0,'blue':0}
file1 = open('input2.txt')
Lines = file1.readlines()
sum1 = 0
for line in Lines:
    game_number = line.split(': ')[0]
    game_number = game_number.split()[1]
    line = line.split(': ')[1]
    splitted = splitLine(line)
    for i in range(len(splitted)):
        updateCount(splitted[i].split(', '))
    print(game_number,dict1)
    sum1 += checkAns()
    print(checkAns())
    dict1['red'], dict1['green'], dict1['blue'] = 0,0,0
    

print(sum1)