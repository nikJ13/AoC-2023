# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:07:18 2024

@author: niket
"""

def FindSum(input_dict):
    sum1 = 0
    for item in input_dict:
        sum1 += input_dict[item]
    return sum1

def ConditionSatisfy(condition,input_dict):
    if condition=="None":
        return True
    var,operator,number = condition[0],condition[1],condition[2:]
    number = int(number)
    if operator==">":
        if input_dict[var]>number:
            return True
    elif operator=="<":
        if input_dict[var]<number:
            return True
    return False

def ProcessingInput(line):
    line = line[1:-1].split(',')
    dict1 = {}
    for inputs in line:
        dict1[inputs[0]] = int(inputs[2:])
    return dict1

def PerformOperation(input_line):
    processed_input = ProcessingInput(input_line)
    #print(processed_input)
    current = "in"
    while True:
        if current=="A":
            ans = FindSum(processed_input)
            return ans
        elif current == "R":
            return 0
        for items in workflows[current]:
            if ConditionSatisfy(items,processed_input):
                current = workflows[current][items]
                break

def StoreDict(string):
    ind_of_bracket = string.index("{")
    workflow_name = string[:ind_of_bracket]
    workflows[workflow_name] = {}
    filters = string[ind_of_bracket+1:-1].split(',')
    for item in range(len(filters)-1):
        condition,destination = filters[item].split(':')
        workflows[workflow_name][condition] = destination
    workflows[workflow_name]["None"] = filters[-1]
    return

file1 = open('input19.txt')
Lines = file1.readlines()
workflows = {}

#print(Lines)

flag = 0
ans = 0
for line in Lines:
    if line=='\n':
        flag+=1
        continue
    if flag==0:
        StoreDict(line.strip())
    else:
        #print(workflows)
        ans += PerformOperation(line.strip())

print(ans)
    