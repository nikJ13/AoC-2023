# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:21:05 2023

@author: niket
"""

def calculateVal(string):
    val = 0
    for ch in string:
        temp = ord(ch)
        val += temp
        val *= 17
        val = val % 256
    return val



file1 = open('input15.txt')
Lines = file1.readlines()

input_list = Lines[0].split('\n')[0].split(',')

#print(input_list)

ans = 0
for hash_input in input_list:
    ans += calculateVal(hash_input)

print(ans)