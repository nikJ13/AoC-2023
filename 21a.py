# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:28:59 2024

@author: niket
"""


file1 = open('input21.txt')
Lines = file1.readlines()
matrix = []

for line in Lines:
    matrix.append(list(line.strip()))

rownum = len(matrix)
colnum = len(matrix[0])

flag = 0
for i in range(rownum):
    for j in range(colnum):
        if matrix[i][j] == 'S':
            break
    else:
        continue
    break

que = [(i,j)]
count = 0

while count!=64:
    k = len(que)
    for i in range(k):
        node = que.pop(0)
        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_x = node[0]+x
            new_y = node[1]+y
            if 0<=new_x<rownum and 0<=new_y<colnum and matrix[new_x][new_y]!='#' and matrix[new_x][new_y]!='O':
                matrix[new_x][new_y] = 'O'
                que.append((new_x,new_y))
        matrix[node[0]][node[1]] = '.'
    count += 1
    #print(count)
    
ans = 0
for i in range(rownum):
    for j in range(colnum):
        if matrix[i][j]=='O':
            ans += 1

print(ans)

# if y<0, then y==colnum