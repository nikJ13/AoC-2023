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
        #print(text1)
        if dict1[text1[1]]<=int(text1[0]):
            dict1[text1[1]] = int(text1[0])
    return

def checkAns():
    if dict1['red']>12 or dict1['green']>13 or dict1['blue']>14:
        return False
    return True

dict1 = {'red':0,'green':0,'blue':0}
file1 = open('input2.txt')
Lines = file1.readlines()
sum1 = 0
for line in Lines:
    game_number = line.split(': ')[0]
    #print(game_number)
    game_number = game_number.split()[1]
    line = line.split(': ')[1]
    #print(line)
    splitted = splitLine(line)
    for i in range(len(splitted)):
        updateCount(splitted[i].split(', '))
    print(game_number,dict1)
    if checkAns():
        print(game_number)
        sum1 += int(game_number)
    dict1['red'], dict1['green'], dict1['blue'] = 0,0,0
    

print(sum1)

1,6,7,10,12,13,14,15,16,17