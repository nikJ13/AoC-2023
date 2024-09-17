# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:36:16 2024

@author: niket
"""

import sys

file1 = open('input23.txt')
Lines = file1.readlines()
matrix = []

for line in Lines:
    matrix.append(list(line.strip()))
    
colnum = len(matrix[0])
rownum = len(matrix)

#print(matrix)

start = (0,matrix[0].index("."))
end = (rownum-1,matrix[-1].index("."))

#print(matrix[-1].index("."))

cross_roads = [start,end] #there are some nodes where it is connected to three neighbors


flag = 0

for i in range(rownum):
    for j in range(colnum):
        if matrix[i][j]=="#":
            continue
        flag = 0
        for x_dir,y_dir in [(1,0),(0,-1),(0,1),(-1,0)]:
            xx = i + x_dir
            yy = j + y_dir
            if 0<=xx<rownum and 0<=yy<colnum and matrix[xx][yy]!="#":
                flag +=1
        if flag>=3:
            cross_roads.append((i,j))
            
#print(cross_roads)
#sys.exit(0)

new_graph = {node:{} for node in cross_roads}

#print(new_graph)


for sr,sc in cross_roads: #mapping all the cross_road nodes to eachother in a directed manner, thereby shortening the graph
    stack = [(sr,sc,0)]   # this method is called edge reduction
    seen = {(sr,sc)}
    #print(sr,sc)
    #print(seen)
    while stack:
        #print(stack)
        row,col,step = stack.pop()
        if step!=0 and (row,col) in cross_roads:
            new_graph[(sr,sc)][(row,col)] = step
            continue
        for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]:
            nr = dr + row
            nc = dc + col
            if 0<=nr<rownum and 0<=nc<colnum and matrix[nr][nc]!="#" and (nr,nc) not in seen:
                stack.append((nr,nc,step+1))
                seen.add((nr,nc))
                
#print(new_graph)
#sys.exit(0)
    
ans = 0

seen_set = set()
            
def dfs(source):  # here, we traverse through the shortened graph, to calculate the steps taken to reach each node
    if source==end:
        return 0
    temp = -float("inf")
    seen_set.add(source)
    for destinations in new_graph[source]:
        if destinations not in seen_set:
            temp = max(temp,dfs(destinations)+new_graph[source][destinations])
    seen_set.remove(source)
    return temp

ans = dfs(start)

print(ans)

    
                


