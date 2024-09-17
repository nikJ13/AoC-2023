# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:57:38 2023

@author: niket
"""

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

for c in range(cols):
    dots = []
    for r in range(rows):
        if matrix[r][c] == 'O':
            if len(dots)==0: # if no empty space till now, then the current position is the best
                stones.append(rows - (r+1) + 1)
            else:
                last_empty = dots.pop(0)
                stones.append(rows - (last_empty+1) + 1)
                dots.append(r)
        elif matrix[r][c]=='.':
            dots.append(r)
        elif matrix[r][c] == '#':
            dots = []
            
ans += sum(stones)

print(ans)
            