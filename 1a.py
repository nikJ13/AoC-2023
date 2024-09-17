# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:55:45 2023

@author: niket
"""

def checkFirst(text):
    n = len(text)
    i = 0
    while(i<n):
        #print(i)
        if text[i].isnumeric():
            break
        elif text[i]=='z':
            end = i+len(words[0])
            if end<n and text[i:end]=='zero':
                return 0
        elif text[i]=='o':
            end = i + len(words[1])
            if end<n and text[i:end]=='one':
                return 1
        elif text[i]=='e':
            end = i + len(words[8])
            if end<n and text[i:end]=='eight':
                return 8
        elif text[i]=='n':
            end = i + len(words[9])
            if end<n and text[i:end]=='nine':
                return 9
        elif text[i]=='t':
            end1 = i + len(words[2])
            end2 = i + len(words[3])
            if end1<n and text[i:end1]=='two':
                return 2
            elif end2<n and text[i:end2]=='three':
                return 3
        elif text[i]=='f':
            end1 = i + len(words[4])
            end2 = i + len(words[5])
            if end1<n and text[i:end1]=='four':
                return 4
            elif end2<n and text[i:end2]=='five':
                return 5
        elif text[i]=='s':
            end1 = i + len(words[6])
            end2 = i + len(words[7])
            if end1<n and text[i:end1]=='six':
                return 6
            elif end2<n and text[i:end2]=='seven':
                return 7
        i+=1
    return text[i]

#eightwo

def checkLast(text):
    n = len(text)
    i = n-1
    while i>=0:
        if text[i].isnumeric():
            break
        elif text[i]=='o':
            start1 = i - len(words[0]) + 1
            start2 = i - len(words[2]) + 1
            if start1>=0 and text[start1:i+1]=='zero':
                return 0
            elif start2>=0 and text[start2:i+1]=='two':
                return 2
        elif text[i]=='r':
            start1 = i - len(words[4]) + 1
            if start1>=0 and text[start1:i+1]=='four':
                return 4
        elif text[i]=='x':
            start1 = i - len(words[6]) + 1
            if start1>=0 and text[start1:i+1]=='six':
                return 6
        elif text[i]=='n':
            start1 = i - len(words[7]) + 1
            if start1>=0 and text[start1:i+1]=='seven':
                return 7
        elif text[i]=='t':
            start1 = i - len(words[8]) + 1
            if start1>=0 and text[start1:i+1]=='eight':
                return 8
        elif text[i]=='e':
            start1 = i - len(words[1]) + 1
            start2 = i - len(words[3]) + 1
            start3 = i - len(words[5]) + 1
            start4 = i - len(words[9]) + 1
            if start1>=0 and text[start1:i+1]=='one':
                return 1
            elif start2>=0 and text[start2:i+1]=='three':
                return 3
            elif start3>=0 and text[start3:i+1]=='five':
                return 5
            elif start4>=0 and text[start4:i+1]=='nine':
                return 9
        i-=1
    return text[i]

file1 = open('input.txt')
Lines = file1.readlines()
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
sum1 = 0

for line in Lines:
    print(line)
    first = checkFirst(line.strip())
    print(first)
    last = checkLast(line.strip())
    sum1 += (int(first)*10)+int(last)

print(sum1)