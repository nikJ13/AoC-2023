# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:25:04 2024

@author: niket
"""
from heapq import heappush,heappop,heapify


file1 = open('test_input17.txt')
Lines = file1.readlines()
matrix = []

matrix = [list(line.strip()) for line in Lines]

rownum = len(matrix)
colnum = len(matrix[0])

# (cost,x,y,x_dir,y_dir,flag)

que = [(0,0,0,0,0,0)]

heapify(que)

visited = set()

while que:
    cost,x,y,x_curr_dir,y_curr_dir,flag = heappop(que)
    
    if x==rownum-1 and y==colnum-1: #in heap queue, the node is stored in the order of the first element in each of the set
        print(cost)                 # hence, here, when the last node is reached, we get the cost of it, which will be the
        break                       # the first element in the queue
    
    if (x,y,x_curr_dir,y_curr_dir,flag) in visited: #checking if the current node has been visited in the same direction
        continue                                    #multiple times or not
    
    visited.add((x,y,x_curr_dir,y_curr_dir,flag)) #adding the current node as visited
    
    if flag<3 and (x_curr_dir,y_curr_dir)!=(0,0): #here, we first check if the direction currently going does not exceed 3 (as given in the problem statement)
        x_dash = x+x_curr_dir                     #here, the second condition (after 'and') checks if there is no direction defined; in the case of starting
        y_dash = y+y_curr_dir                     # the traversal, we are in the idle state, hence this whole if block statement will not execute for the first node of the matrix
        if 0<=x_dash<rownum and 0<=y_dash<colnum: #checking if present in range or not
            heappush(que,(int(matrix[x_dash][y_dash])+cost,x_dash,y_dash,x_curr_dir,y_curr_dir,flag+1))
        
    for xdir,ydir in [(1,0),(0,1),(-1,0),(0,-1)]:
        if (xdir,ydir)!=(x_curr_dir,y_curr_dir) and (xdir,ydir)!=(-x_curr_dir,-y_curr_dir): #here, the first condition checks if the direction in the for loop is not equal to the current direction
            x_dash = x+xdir                                                                 #such condition is given as this check has already been done by the if statement before 
            y_dash = y+ydir                                                                 #the second condition ensures the node before the current one is not traversed, as it would be the opposite direction    
            if 0<=x_dash<rownum and 0<=y_dash<colnum:
                heappush(que,(int(matrix[x_dash][y_dash])+cost,x_dash,y_dash,xdir,ydir,1))
            