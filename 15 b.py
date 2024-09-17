# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:21:05 2023

@author: niket
"""

class Node:
    
    def __init__(self):
        self.next = None
        self.prev = None
        self.valnum = 0
        self.valchar = 0
    
    def add(self,current_node,tailed):
        previous = tailed.prev
        previous.next = current_node
        current_node.prev = previous
        current_node.next = tailed
        tailed.prev = current_node
    
    def remove(self,current_node):
        previous = current_node.prev
        next_node = current_node.next
        previous.next = next_node
        next_node.prev = previous
        current_node.prev = None
        current_node.next = None


def calculateVal(string):
    val = 0
    for ch in string:
        if ch=='=' or ch=='-':
            break
        temp = ord(ch)
        val += temp
        val *= 17
        val = val % 256
    return val

def insertVal(num,arr,string):
    label,lens = string.split('=')
    if arr[num]==0:
        new_node = Node()
        new_node.valchar = label
        new_node.valnum = lens
        head = Node()
        head.valchar = -1
        head.valnum = -1
        tail = Node()
        tail.valchar = -1
        tail.valnum = -1
        head.next = tail
        tail.prev = head
        arr[num] = head
        new_node.add(new_node,tail)
        #print(arr[num].valchar)
        #print(arr[num].next.valchar)
    else:
        curr = arr[num].next
        flag = 0
        while curr.valchar!=-1:
            if curr.valchar==label:
                curr.valnum = lens
                flag = 1
                break
            curr = curr.next
        if flag==0:
            new_node = Node()
            new_node.valchar,new_node.valnum = label,lens
            new_node.add(new_node,curr)
            #print('here')
            #print(curr.prev.valchar)
            #print(curr.valchar)
        
def removeVal(num,arr,string):
    label = string.split('-')[0]
    if arr[num]!=0:
        curr = arr[num].next
        while curr.valchar!=-1:
            if curr.valchar==label:
                curr.remove(curr)
                break
            curr = curr.next

def focus(box_num,curr_node):
    temp = 0
    count = 1
    #print("inside")
    while curr_node.valchar!=-1:
        temp += (box_num+1)*(count)*(int(curr_node.valnum))
        #print(r)
        #print(curr_node.valchar)
        count += 1
        curr_node = curr_node.next
    return temp



file1 = open('input15.txt')
Lines = file1.readlines()

input_list = Lines[0].split('\n')[0].split(',')
boxes = [0]*256

#print(input_list)

ans = 0
for hash_input in input_list:
    box_number = calculateVal(hash_input)
    if hash_input[-1]=='-':
        removeVal(box_number,boxes,hash_input)
    else:
        insertVal(box_number,boxes,hash_input)
        
for box_count in range(len(boxes)):
    if boxes[box_count]!=0:
        #print("outside")
        ans += focus(box_count,boxes[box_count].next)
        #print(t)
#print(boxes)
'''test_node = boxes[0]
while test_node!=None:
    print(test_node.valchar)
    test_node = test_node.next

test2 = boxes[1]
while test2!=None:
    print(test2.valchar)
    test2 = test2.next
    
test3 = boxes[3]
while test3!=None:
    print(test3.valnum)
    test3 = test3.next'''
    #ans += calculateVal(hash_input)

print(ans)