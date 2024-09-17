# Here, the assumption is that every other pipe apart from the loop does not mislead to any other path

file1 = open('input10.txt')
Lines = file1.readlines()
matrix = []

dirs = {
        "|":[(1,0),(-1,0)],
        "-":[(0,1),(0,-1)],
        "L":[(-1,0),(0,1)],
        "J":[(-1,0),(0,-1)],
        "7":[(1,0),(0,-1)],
        "F":[(1,0),(0,1)],
        "S":[(0,1),(1,0),(-1,0),(0,-1)]
        }

for line in Lines:
    matrix.append(list(line.strip()))
    
#print(matrix)

rownum = len(matrix)
colnum = len(matrix[0])

for i in range(rownum):
    for j in range(colnum):
        if matrix[i][j]=="S":
            break
    else:         #here, incase the inner loop breaks, then it skips the else here and executes the break after that
        continue
    break

start = (i,j)

que = [start]

seen = [start]

while que:
    k = len(que)
    for i in range(k):
        x,y = que.pop(0)
        for x_dir,y_dir in dirs[matrix[x][y]]:
            xx = x + x_dir
            yy = y + y_dir
            if 0<=xx<=rownum and 0<=yy<=colnum and (xx,yy) not in seen and matrix[xx][yy]!=".":
                seen.append((xx,yy))
                que.append((xx,yy))

print(len(seen)//2)
            
        


# def recurse(node,seen_arr,cycle):
#     x,y = node
#     if x<0 or x>=rownum or y<0 or y>=colnum or (node in seen_arr and matrix[x][y]!="S"):
#         return cycle,0
#     if node in seen_arr:
#         cycle = seen_arr
#         return cycle,1
#     seen_arr.append(node)
#     ans = []
#     for x_dir,y_dir in dirs[matrix[x][y]]:
#         xx = x + x_dir
#         yy = y + y_dir
#         if 0<=xx<=rownum and 0<=yy<=colnum and (xx,yy) not in seen_arr and matrix[xx][yy]!=".":
#             ans,flag = recurse((xx,yy),seen_arr,cycle)
#             if flag==1:
#                 seen_arr.pop()
#                 return ans,1
#     seen_arr.pop()
#     return ans,0

# print(recurse(start,[],[]))


#print(cycle)
        
        