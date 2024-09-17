

file1 = open('C:/Niket/AoC/input18.txt')
Lines = file1.readlines()
points = [(0,0)]
directions = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
boundary_points = 0

for line in Lines:
    dirs,num,color = line.strip().split()
    delta_x,delta_y = directions[dirs]
    x,y = points[-1]
    new_x,new_y = x+(int(num)*delta_x),y+(int(num)*delta_y)
    points.append((new_x,new_y))
    boundary_points += int(num)
    

#implementing the shoelace theorem
Area = abs(sum(points[i][0]*(points[i-1][1]-points[(i+1)%len(points)][1]) for i in range(len(points))))//2

print(Area)
#using pick's theorem
interior_points = Area - (boundary_points//2) + 1

print(interior_points+boundary_points)
