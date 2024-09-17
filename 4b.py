# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:08:12 2023

@author: niket
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:27:34 2023

@author: niket
"""

from collections import defaultdict

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

def getCards(winList,normalList,num):
    matches = 0
    for i in winList:
        if i in normalList:
            matches += 1
    for count in range(1,matches+1):
        dict_copies[num+count] = dict_copies[num+count] + dict_copies[num]
    return dict_copies[num]
    
    

def getNumbers(text,number):
    text1 = removeCardNumber(text)
    win_numbers, normal_numbers = splitNumbers(text1)
    return getCards(win_numbers, normal_numbers,number)

cards = 0
dict_copies = defaultdict(lambda:1)
dict_copies[1] = 1
file1 = open('input4.txt')
Lines = file1.readlines()
card_number = 1
for line in Lines:
    cards += getNumbers(line.strip(),card_number)
    card_number += 1

print(cards)