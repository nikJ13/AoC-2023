# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:22:58 2023

@author: niket
"""

file1 = open('input9.txt')
Lines = file1.readlines()
ans = 0

def reading(text):
    text = text.split()
    return [int(i) for i in text]

def recurse(arr1):
    n = len(arr1)
    diff = [arr1[i]-arr1[i-1] for i in range(1,n)]
    #print(diff)
    if all(j==0 for j in diff):
        return arr1[-1]
    else:
        return arr1[0]-recurse(diff)
    

for line in Lines:
    line = line.strip()
    arr = reading(line)
    temp = recurse(arr)
    #print(temp)
    ans = ans + temp
    
print(ans)