# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:57:38 2023

@author: niket
"""

import copy


file1 = open('input14.txt')
Lines = file1.readlines()
stones = []
stone_count = 0
ans = 0
matrix = []

for line in Lines:
    matrix.append(list(line.strip()))

rows = len(matrix)
cols = len(matrix[0])

# for c in range(cols):
#     dots = []
#     for r in range(rows):
#         if matrix[r][c] == 'O':
#             if len(dots)==0: # if no empty space till now, then the current position is the best
#                 stones.append(rows - (r+1) + 1)
#             else:
#                 last_empty = dots.pop(0)
#                 stones.append(rows - (last_empty+1) + 1)
#                 dots.append(r)
#         elif matrix[r][c]=='.':
#             dots.append(r)
#         elif matrix[r][c] == '#':
#             dots = []
            
# ans += sum(stones)

# print(ans)

def northBend():
    que = [[] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==".":
                que[j].append((i,j))
            elif matrix[i][j]=="O":
                if que[j]:
                    x,y = que[j].pop(0)
                    matrix[x][y] = "O"
                    matrix[i][j] = "."
                    que[j].append((i,j))
            elif matrix[i][j]=="#":
                que[j] = []
    #print(matrix)
    return

def westBend():
    que = [[] for _ in range(rows)]
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j]==".":
                que[i].append((i,j))
            elif matrix[i][j]=="O":
                if que[i]:
                    x,y = que[i].pop(0)
                    matrix[x][y] = "O"
                    matrix[i][j] = "."
                    que[i].append((i,j))
            elif matrix[i][j]=="#":
                que[i] = []
    #print(matrix)
    return

def southBend():
    que = [[] for _ in range(cols)]
    for i in range(rows-1,-1,-1):
        for j in range(cols):
            if matrix[i][j]==".":
                que[j].append((i,j))
            elif matrix[i][j]=="O":
                if que[j]:
                    x,y = que[j].pop(0)
                    matrix[x][y] = "O"
                    matrix[i][j] = "."
                    que[j].append((i,j))
            elif matrix[i][j]=="#":
                que[j] = []
    #print(matrix)
    return

def eastBend():
    que = [[] for _ in range(rows)]
    for j in range(cols-1,-1,-1):
        for i in range(rows):
            if matrix[i][j]==".":
                que[i].append((i,j))
            elif matrix[i][j]=="O":
                if que[i]:
                    x,y = que[i].pop(0)
                    matrix[x][y] = "O"
                    matrix[i][j] = "."
                    que[i].append((i,j))
            elif matrix[i][j]=="#":
                que[i] = []
    #print(matrix)
    return

def calculateLoad(arr):
    count = rows+1
    ans = 0
    for i in range(rows):
        count -= 1
        num = 0
        for j in range(cols):
            if arr[i][j]=="O":
                num += 1
        ans = ans + num*count
    return ans

mat_first = copy.deepcopy(matrix)
seen = [mat_first]

for i in range(1000000000):
    northBend()
    westBend()
    southBend()
    eastBend()
    if matrix in seen:
        break
    matt = copy.deepcopy(matrix)
    seen.append(matt)
    
first = seen.index(matrix)
print("first occurrence:",first)
print("repeats after:",i)

keep = seen[(1000000000-first)%(i+1-first)+first]
#print(matrix)
print(calculateLoad(keep))