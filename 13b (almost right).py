# # -*- coding: utf-8 -*-
# """
# Created on Fri Dec 15 15:24:09 2023

# @author: niket
# """

# # -*- coding: utf-8 -*-
# """
# Created on Fri Dec 15 12:27:39 2023

# @author: niket
# """

# def symmetryVertical(arr,col_num1,col_num2,n,m,smudgeFlag):
#     if col_num1<0 or col_num2>=n:
#         return True
#     t1 = [arr[i][col_num1] for i in range(m)]
#     t2 = [arr[i][col_num2] for i in range(m)]
#     if t1==t2:
#         return symmetryVertical(arr, col_num1-1, col_num2+1, n, m, smudgeFlag)
#     else:
#         if smudgeFlag==0:
#             for r in range(m):
#                 t = t1[r][col_num1]
#                 if t1[r][col_num1]==".":
#                     t1[r][col_num1] = "#"
#                 else:
#                     t1[r][col_num1] = "."
#                 if t1==t2:
#                     return symmetryVertical(arr,col_num1-1,col_num2+1,n,m,1)
#                 else:
#                     t1[r][col_num1] = t
#         return False

# def symmetryHorizontal(arr,row_num1,row_num2,n,m):
#     if row_num1<0 or row_num2>=m:
#         return True
#     t1 = [arr[row_num1][j] for j in range(n)]
#     t2 = [arr[row_num2][j] for j in range(n)]
#     if t1==t2:
#         return symmetryHorizontal(arr, row_num1-1, row_num2+1, n, m)
#     else:
#         return False

# def checkVertical(arr):
#     rows = len(arr)
#     cols = len(arr[0])
#     for c in range(0,cols-1):
#         temp1 = [arr[r][c] for r in range(rows)]
#         temp2 = [arr[r][c+1] for r in range(rows)]
#         if temp1==temp2:
#             if symmetryVertical(arr,c-1,c+2,cols,rows,0):
#                 return True,c
#         else:
#             for r in range(rows):
#                 t = temp1[r][c]
#                 if temp1[r][c]==".":
#                     temp1[r][c] = "#"
#                 else:
#                     temp1[r][c] = "."
#                 if temp1==temp2:
#                     checkSmudge = 1
#                     if symmetryVertical(arr,c-1,c+2,cols,rows,checkSmudge):
#                         return True,c
#                 else:
#                     temp1[r][c] = t
#     return False,-1
        
# def checkHorizontal(arr):
#     rows = len(arr)
#     cols = len(arr[0])
#     for r in range(0,rows-1):
#         temp1 = [arr[r][c] for c in range(cols)]
#         temp2 = [arr[r+1][c] for c in range(cols)]
#         if temp1==temp2:
#             if symmetryHorizontal(arr,r-1,r+2,cols,rows):
#                 return True,r
#     return True,-1


# def changeMatrix(matrix):
#     nr = len(matrix)
#     nc = len(matrix[0])
#     for i in range(nr):
#         for j in range(nc):
#             temp = matrix[i][j]
#             if temp=='.':
#                 matrix[i][j] = '#'
#             elif temp=='#':
#                 matrix[i][j] = '.'
#             flag1, col = checkVertical(matrix)
#             if flag1:
#                 return col + 1
#             flag2, row = checkHorizontal(matrix)
#             if flag2:
#                 return 100*(row+1)
#             matrix[i][j] = temp
            

# file1 = open('input13.txt')
# Lines = file1.readlines()
# ans = 0
# line_count = 0

# # while line_count<len(Lines):
# #     matrix = []
# #     while line_count<len(Lines) and Lines[line_count]!='\n':
# #         matrix.append(list(Lines[line_count].strip()))
# #         line_count += 1
# #     ans += changeMatrix(matrix)
# #     line_count += 1

# # print(ans)

# while line_count<len(Lines):
#     matrix = []
#     while line_count<len(Lines) and Lines[line_count]!='\n':
#         matrix.append(list(Lines[line_count].strip()))
#         line_count += 1
#     flag, col = checkVertical(matrix)
#     if flag:
#         ans += col+1
#     else:
#         ans += 100*(checkHorizontal(matrix)+1)
#     line_count += 1

# print(ans)

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

total = 0

for block in open("input13.txt").read().split("\n\n"):
    grid = block.splitlines()

    row = find_mirror(grid)
    total += row * 100

    col = find_mirror(list(zip(*grid)))
    total += col

print(total)