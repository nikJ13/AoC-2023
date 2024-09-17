# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:24:07 2024

@author: niket
"""

def checkIntersection(b1,b2):
    return max(b1[0],b2[0])<=min(b1[3],b2[3]) and max(b1[1],b2[1])<=min(b1[4],b2[4])


file1 = open('test_input22.txt')
Lines = file1.readlines()
matrix = []

for line in Lines:
    matrix.append(list(map(int,line.strip().replace('~',',').split(','))))
    
matrix.sort(key = lambda matrix:matrix[2])

#first determining the final positions of the bricks after falling

for index,brick in enumerate(matrix):
    max_z_to_reach = 1
    for prev_bricks in matrix[:index]:
        if checkIntersection(prev_bricks,brick):
            max_z_to_reach = max(max_z_to_reach,prev_bricks[5]+1)        
    
    brick[5] = (brick[5]-brick[2]) + max_z_to_reach
    brick[2] = max_z_to_reach
    
# arranging the bricks again since they might have changed their order after settling

matrix.sort(key = lambda matrix:matrix[2])

# this dictionary means the key brick supports the following value bricks

key_supports_val = {i: set() for i in range(len(matrix))}

# this dictionary means the value bricks support the key bricks

val_supports_key = {i: set() for i in range(len(matrix))}

for i,upper in enumerate(matrix):
    for j,lower in enumerate(matrix[:i]):
        if checkIntersection(lower,upper) and upper[2]==lower[5]+1:
            key_supports_val[j].add(i)
            val_supports_key[i].add(j)
        
ans = 0

for lower_bricks in key_supports_val:
    # checking if the lower brick that is providing support is the only brick for the value brick which provides support
    if all(len(val_supports_key[j])>=2 for j in key_supports_val[lower_bricks]):
        ans += 1

print(key_supports_val)

print(val_supports_key)

print(matrix)

print(ans)