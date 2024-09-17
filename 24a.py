# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:29:55 2024

@author: niket
"""

file1 = open('input24.txt')
Lines = file1.readlines()
matrix = []


for line in Lines:
    position,velocities = line.strip().split(" @ ")
    x,y,z = list(map(int,position.split(", ")))
    xv,yv,zv = list(map(int,velocities.split(", ")))
    slope = yv/xv #m
    y_intercept = y - (slope*x) #b
    matrix.append((slope,y_intercept,x,y,xv,yv))

lower_limit = 200000000000000
upper_limit = 400000000000000
ans = 0

for index,point1 in enumerate(matrix):
    m1,b1,sx1,sy1,xv1,yv1 = point1
    for point2 in matrix[index+1:]:
        m2,b2,sx2,sy2,xv2,yv2 = point2
        if m1==m2:
            continue
        xx = (b2-b1)/(m1-m2)
        yy = (m1*xx) + b1
        if lower_limit<=xx<=upper_limit and lower_limit<=yy<=upper_limit:
            if xv1*(xx-sx1)>=0 and yv1*(yy-sy1)>=0 and xv2*(xx-sx2)>=0 and yv2*(yy-sy2)>=0:
                print(xx,yy)
                ans += 1
        
print(ans)
    
    
    