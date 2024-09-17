# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 00:08:23 2023

@author: niket
"""

file1 = open('input11.txt')
Lines = file1.readlines()
matrix = [list(line.strip()) for line in Lines]

rows = len(matrix)
cols = len(matrix[0])

# checking for empty rows

empty_rows = []
empty_cols = []

gal = []

for i in range(rows):
    empty = True
    for j in range(cols):
        if matrix[i][j]=='#':
            gal.append((i,j))
            empty = False
    if empty:
        empty_rows.append(i)

for i in range(cols):
    empty = True
    for j in range(rows):
        if matrix[j][i]=='#':
            empty = False
    if empty:
        empty_cols.append(i)
        

er = len(empty_rows)
ec = len(empty_cols)
ans = 0

for node1 in range(len(gal)-1):
    for node2 in range(node1+1,len(gal)):
        r,c = 0,0
        distance = abs(gal[node2][0]-gal[node1][0]) + abs(gal[node2][1]-gal[node1][1])
        expansion = 0
        while r<er:
            if min(gal[node1][0],gal[node2][0])<=empty_rows[r]<=max(gal[node1][0],gal[node2][0]):
                expansion += 1
            r += 1
        while c<ec:
            if min(gal[node1][1],gal[node2][1])<=empty_cols[c]<=max(gal[node1][1],gal[node2][1]):
                expansion += 1
            c += 1
        ans = ans + distance + expansion

print(ans)
        
        
            
    


        