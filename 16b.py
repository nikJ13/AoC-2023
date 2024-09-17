import time

file1 = open('input16.txt')
Lines = file1.readlines()
matrix = []

dirs = {
        "|":{"n":[(-1,0,"n")],"s":[(1,0,"s")],"e":[(-1,0,"n"),(1,0,"s")],"w":[(-1,0,"n"),(1,0,"s")]},
        "-":{"n":[(0,-1,"w"),(0,1,"e")],"s":[(0,-1,"w"),(0,1,"e")],"e":[(0,1,"e")],"w":[(0,-1,"w")]},
        "/":{"e":[(-1,0,"n")],"w":[(1,0,"s")],"n":[(0,1,"e")],"s":[(0,-1,"w")]},
        "\\":{"n":[(0,-1,"w")],"s":[(0,1,"e")],"e":[(1,0,"s")],"w":[(-1,0,"n")]}
        }

for line in Lines:
    matrix.append(list(line.strip()))

print(matrix)

rownum = len(matrix)
colnum = len(matrix[0])

ans = 0

def BFS(sx,sy,direct):
    que = [(sx,sy,direct)]
    energised = {(sx,sy,direct)}
    while que:
        k = len(que)
        for i in range(k):
            x,y,direction = que.pop(0)
            if matrix[x][y]==".":
                if direction=="n":
                    path = [(-1,0,"n")]
                elif direction=="s":
                    path = [(1,0,"s")]
                elif direction=="e":
                    path = [(0,1,"e")]
                elif direction=="w":
                    path = [(0,-1,"w")]
            else:
                path = dirs[matrix[x][y]][direction]
            for x_dir,y_dir,future_dir in path:
                xx = x + x_dir
                yy = y + y_dir
                if 0<=xx<rownum and 0<=yy<colnum and (xx,yy,future_dir) not in energised: # this condition is to make sure not to track the ray of light that is going in constant loop
                    energised.add((xx,yy,future_dir))
                    que.append((xx,yy,future_dir))
        
    conc = {(r,c) for (r,c,_) in energised} # getting only the positions
    return len(conc)

for i in range(colnum):
    if i==0:
        ans = max(ans,BFS(0,i,"e"))
        ans = max(ans,BFS(rownum-1,i,"e"))
    elif i==colnum-1:
        ans = max(ans,BFS(0,i,"w"))
        ans = max(ans,BFS(rownum-1,i,"w"))
    ans = max(ans,BFS(0,i,"s"))
    ans = max(ans,BFS(rownum-1,i,"n"))

for j in range(rownum):
    if j==0 or j==rownum-1:
        continue
    ans = max(ans,BFS(j,0,"e"))
    ans = max(ans,BFS(j,colnum-1,"w"))

print(ans)
        