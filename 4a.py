# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:27:34 2023

@author: niket
"""

def removeCardNumber(st):
    return st.split(': ')[1]

def splitNumbers(st):
    l1 = st.split(' | ')[0]
    l2 = st.split(' | ')[1]
    list1 = l1.split()
    list2 = l2.split()
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    for i in range(len(list2)):
        list2[i] = int(list2[i])
    return list1, list2

def getPoints(winList,normalList):
    matches = 0
    for i in winList:
        if i in normalList:
            matches += 1
    if matches==0:
        return 0
    else:
        return 2**(matches-1)

def getNumbers(text):
    text1 = removeCardNumber(text)
    win_numbers, normal_numbers = splitNumbers(text1)
    return getPoints(win_numbers, normal_numbers)

points = 0
file1 = open('input4.txt')
Lines = file1.readlines()
for line in Lines:
    points += getNumbers(line.strip())

print(points)