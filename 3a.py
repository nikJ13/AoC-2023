# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:58:27 2023

@author: niket
"""
import re


def setupMatrix(text):
    element = []
    i,j = 0,0
    n = len(text)
    numbers = re.findall(r'\d+', text)
    while(i<n):
        if text[i].isnumeric()!=True:
            element.append(text[i])
            i+=1
        else:
            element.append(numbers[j])
            j+=1
            while(i<n and text[i].isnumeric()):
                i+=1
        print(i)
    matrix.append(element)
    
def traverseLine(matrix,ind):
    ans = 0
    #checking for the first element
    if matrix[ind][0].isnumeric():
        #for first row
        if ind==0 and ((matrix[ind][1]!='.' and matrix[ind][1].isnumeric()!=True) or (matrix[ind+1][1]!='.' and matrix[ind+1][1].isnumeric()!=True)):
            ans = ans + int(matrix[ind][0])
        #for last row
        elif ind==m-1 and ((matrix[ind][1]!='.' and matrix[ind][1].isnumeric()!=True) or (matrix[ind-1][1]!='.' and matrix[ind-1][1].isnumeric()!=True)):
            ans = ans + int(matrix[ind][0])
    #checking for the last element
    if matrix[ind][-1].isnumeric():
        #for the first row
        if ind==0 and ((matrix[ind][-2]!='.' and matrix[ind][-2].isnumeric()!=True) or (matrix[ind+1][-2]!='.' and matrix[ind+1][-2].isnumeric()!=True)):
            ans = ans + int(matrix[ind][-1])
        elif ind==m-1 and ((matrix[ind][-2]!='.' and matrix[ind][-2].isnumeric()!=True) or (matrix[ind-1][-2]!='.' and matrix[ind-1][-2].isnumeric()!=True)):
            ans = ans + int(matrix[ind][0])
    for i in range(1,len(matrix[ind])-1):
        if matrix[ind][i].isnumeric() and ((matrix[ind][i-1].isnumeric()!=True and matrix[ind][i-1]!='.') or (matrix[ind][i+1].isnumeric()!=True and matrix[ind][i+1]!='.') or (matrix[ind+1][i+1].isnumeric()!=True and matrix[ind+1][i+1]!='.') or (matrix[ind-1][i+1].isnumeric()!=True and matrix[ind-1][i+1]!='.') or (matrix[ind+1][i-1].isnumeric()!=True and matrix[ind+1][i-1]!='.') or (matrix[ind-1][i-1].isnumeric()!=True and matrix[ind-1][i-1]!='.')):
            ans = ans + int(matrix[ind][i])
    return ans
        
def diagonalCheck(matrix,index):
    ans = 0
    if matrix[index][0].isnumeric() and ((matrix[index][1]!='.' and matrix[index][1].isnumeric()!=True) or (matrix[index-1][1]!='.' and matrix[index-1][1].isnumeric()!=True) or (matrix[index+1][1]!='.' and matrix[index+1][1].isnumeric()!=True)):
        ans = ans + int(line1[0])
    if matrix[index][0].isnumeric() and ((matrix[index][1]!='.' and matrix[index][1].isnumeric()!=True) or (matrix[index-1][1]!='.' and matrix[index-1][1].isnumeric()!=True) or (matrix[index+1][1]!='.' and matrix[index+1][1].isnumeric()!=True)):
        ans = ans + int(line1[-1])
    for i in range(1,len(line1)-1):
        if line1[i].isnumeric() and ((line1[i-1].isnumeric()!=True and line1[i-1]!='.') or (line1[i+1].isnumeric()!=True and line1[i+1]!='.')):
            ans = ans + int(line1[i])
    return ans
    


matrix = []
file1 = open('input3.txt')
Lines = file1.readlines()
sum1 = 0
for line in Lines:
    setupMatrix(line.strip())

print(matrix)
m = len(matrix)
for j in range(m):
    sum1 += traverseLine(matrix,j)
    
print(sum1)

#print(matrix)

