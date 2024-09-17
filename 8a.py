# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:06:12 2023

@author: niket
"""

from collections import defaultdict

file1 = open('input8.txt')
Lines = file1.readlines()

instructions = Lines[0].strip()
length_instruct = len(instructions)
counter = 0
dict_map = defaultdict(list)

for line_num in range(2,len(Lines)):
    key,values = Lines[line_num].split(" = ")[0],Lines[line_num].split(" = ")[1]
    values = values.strip("()\n")
    val1,val2 = values.split(", ")[0],values.split(", ")[1]
    dict_map[key] = [val1,val2]
    #print(key)
    #print(dict_map[key])
    
tracker = 'AAA'
ans = 0
while True:
    if tracker=='ZZZ':
        print(ans)
        break
    follow = instructions[counter]
    if follow=='L':
        tracker = dict_map[tracker][0]
    else:
        tracker = dict_map[tracker][1]
    ans += 1
    counter = (counter + 1)%length_instruct
        
    

    