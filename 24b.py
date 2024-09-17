# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:50:12 2024

@author: niket
"""

import sympy

file1 = open('input24.txt')
Lines = file1.readlines()
matrix = []

for line in Lines:
    position,velocities = line.strip().split(" @ ")
    x,y,z = list(map(int,position.split(", ")))
    xv,yv,zv = list(map(int,velocities.split(", ")))
    matrix.append((x,y,z,xv,yv,zv))

xr,yr,zr,vxr,vyr,vzr = sympy.symbols("xr,yr,zr,vxr,vyr,vzr")

equations = []

# since x_intersection = x_current_position + (vx_speed * time)

# the above equation is applicable for the rock that will collide and also the hailstones

# make system of equations and solve them using sympy

for x,y,z,xv,yv,zv in matrix:
    equations.append((x-xr)*(vyr-yv) - (y-yr)*(vxr-xv))
    equations.append((y-yr)*(vzr-zv) - (z-zr)*(vyr-yv))
    
ans = sympy.solve(equations)

print(ans)

print(ans[0][xr]+ans[0][yr]+ans[0][zr])