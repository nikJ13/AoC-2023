def FindNum(string):
    #print(string)
    summation = 0
    power = 4
    for ch in string:
        #print(ch)
        if ch in hexa:
            summation += hexa[ch]*16**power
        else:
            summation += int(ch)*16**power
        power-=1
    return summation


file1 = open('C:/Niket/AoC/input18.txt')
Lines = file1.readlines()
points = [(0,0)]
directions = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
direction_dig = {0:directions["R"],1:directions["D"],2:directions["L"],3:directions["U"]}
hexa = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
boundary_points = 0

for line in Lines:
    dirs,num,color = line.strip().split()
    color = color[2:8]
    #print(color[-1])
    delta_x,delta_y = direction_dig[int(color[-1])]
    x,y = points[-1]
    new_num = FindNum(color[:-1])
    #print(new_num)
    #new_num = int(color[:-1],16)
    #print(new_num)
    new_x,new_y = x+(new_num*delta_x),y+(new_num*delta_y)
    points.append((new_x,new_y))
    boundary_points += new_num
    

#implementing the shoelace theorem
Area = abs(sum(points[i][0]*(points[i-1][1]-points[(i+1)%len(points)][1]) for i in range(len(points))))//2

print(Area)
#using pick's theorem
interior_points = Area - (boundary_points//2) + 1

print(interior_points+boundary_points)
