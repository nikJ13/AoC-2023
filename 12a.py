# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:17:30 2023

@author: niket
"""

def checkValidity(arr,block_num):
    recorded_hash = []
    current_count = 0
    for ch in arr:
        if ch=='#':
            current_count += 1
        elif ch=='.':
            if current_count>0:
                recorded_hash.append(current_count)
            current_count = 0
        else:
            return False
    if current_count>0:
        recorded_hash.append(current_count)
    return recorded_hash == block_num

def recurse(records,blocks,ind):
    if ind==len(records):
        return 1 if checkValidity(records,blocks) else 0
    if records[ind]=='?':
        return recurse(records[:ind]+'#'+records[ind+1:],blocks,ind+1) + recurse(records[:ind]+'.'+records[ind+1:],blocks,ind+1)
    elif records[ind]=='.' or records[ind]=='#':
        return recurse(records,blocks,ind+1)


file1 = open('input12.txt')
Lines = file1.readlines()

ans = 0

for line in Lines:
    record,block = line.strip().split()
    #print(record)
    block = [int(x) for x in block.split(',')]
    #print(block)
    ans += recurse(record,block,0)
    #print(ans)

print(ans)