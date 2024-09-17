# # -*- coding: utf-8 -*-
# """
# Created on Wed Jan 24 19:20:52 2024

# @author: niket
# """

# import sys

# def flipflop(flag_status,incoming_signal,count_low,count_high):
#     if incoming_signal == "low":
#         if flag_status=="off":
#             flag_status = "on"
#             count_high+=1
#             output_signal = "high"
#         else:
#             flag_status = "off"
#             count_low += 1
#             output_signal = "low"
#     else:
#         output_signal = "high"
#         count_high+=1
#     return flag_status,output_signal,count_low,count_high

# def conjunction(curr_source,parent_of_signal,incoming_signal,count_low,count_high):
#     memory[curr_source][parent_of_signal] = incoming_signal
#     if all(val == list(memory[curr_source].values())[0] for val in memory[curr_source].values()):
#         if incoming_signal=="low":
#             output_signal = "high"
#             count_high+=1
#         else:
#             output_signal="low"
#             count_low+=1
#     else:
#         if incoming_signal=="low":
#             output_signal = "low"
#             count_low+=1
#         else:
#             output_signal = "high"
#             count_high+=1
#     return output_signal,count_low,count_high
            

# def recurse(node):
#     for key_val in mapping:
#         if node in mapping[key_val]:
#             memory[node][key_val] = "low"
#             if isinstance(memory[key_val],dict):
#                 recurse(key_val)
#     return

# file1 = open('test_input20.txt')
# Lines = file1.readlines()
# mapping = {}
# memory = {0:"none"}

# for line in Lines:
#     operation_origin,targets = line.strip().split(" -> ")
#     targets_arr = targets.strip().split(', ')
#     if operation_origin!="broadcaster":
#         operation,origin = operation_origin[0],operation_origin[1:]
#         #print(origin)
#         #print(mapping)
#         #print(memory)
#         if operation=="%": #origin,flag_status
#             memory[origin] = "off"
#             mapping[origin] = targets_arr
#         else:
#             memory[origin] = {} 
#             mapping[origin] = targets_arr
#     else:
#         mapping[0] = targets_arr

# for key in memory:
#     if isinstance(memory[key],dict): #if it is conjunction
#         recurse(key)
        
# #print(mapping)
# #print(memory)

# #sys.exit(0)

# ans_low = 0
# ans_high = 0
# lows = 0
# highs = 0
# for j in range(2):
#     #print(i)
#     que = [0]
#     lows+=1
#     signal = {0:["low",-1]} #signal,parent
#     while que:
#         #print(que)
#         k = len(que)
#         for i in range(k):
#             p = que.pop(0)
#             if p==0:
#                 lows += len(mapping[p])
#                 outputs = "low"
#             if p in memory:
#                 #print("here:",p)
#                 #print("there:",mapping[p])
#                 if isinstance(memory[p],dict):
#                     #print("here:",p)
#                     outputs,l,h = conjunction(p,signal[p][1],signal[p][0],0,0)
#                     lows += l*(len(mapping[p]))
#                     highs += h*(len(mapping[p]))
#                     #print("here lows: ",lows," here highs: ",highs)
#                 elif memory[p]!="none":
#                     #print("there:",p)
#                     status,outputs,l,h = flipflop(memory[p],signal[p][0],0,0)
#                     memory[p] = status
#                     lows += l*(len(mapping[p]))
#                     highs += h*(len(mapping[p]))
#                     #print("there lows: ",lows," there highs: ",highs)
#                 for elements in mapping[p]:
#                     signal[elements] = [outputs,p]
#                     que.append(elements)
        
#     print(lows)
#     print(highs)
# print(mapping)
# print(memory)
    
# each module that broadcasts signals is stored as objects, containing information such as name, type, output and memory
class Module:
    
    def __init__(self,name,type,outputs):
        self.name = name
        self.type = type
        self.outputs = outputs
        
        if type=="%":
            self.memory = "off"
        else:
            self.memory = {}
    
    def __repr__(self):
        return f"{self.name}, {self.type}, {self.outputs}, {self.memory}" 
            
modules = {}

broadcaster_destinations = []

file1 = open('input20.txt')
Lines = file1.readlines()

for line in Lines:
    operation_origin,targets = line.strip().split(" -> ")
    targets_arr = targets.strip().split(', ')
    if operation_origin=="broadcaster":
        broadcaster_destinations = targets_arr
    else:
        operation,origin = operation_origin[0],operation_origin[1:]
        modules[origin] = Module(origin,operation,targets_arr)

#print(broadcaster_destinations)
#print(modules)

# populate the memories of the conjunction modules, from where they receive signals

for name,mod in modules.items():
    for output in mod.outputs:
        if output in modules and modules[output].type=="&":
            modules[output].memory[name] = "low"

#print(modules)

low = high = 0

for _ in range(1000):
    #signal,origin,target
    que = [("low","broadcaster",y) for y in broadcaster_destinations]
    low += 1
    #print(que.pop(0))
    while que:
        #print(que)
        signal,origin,target = que.pop(0)
        if signal=="low":
            low += 1
        else:
            high += 1
        if target not in modules:
            continue
        mod_object = modules[target] # destination where the signal is going
        if mod_object.type=="%":   # checking the behaviour of the module once the current signal reaches it
            if signal=="low":
                if mod_object.memory=="off":
                    mod_object.memory = "on"
                    for t in mod_object.outputs:
                        que.append(("high",mod_object.name,t))
                else:
                    mod_object.memory = "off"
                    for t in mod_object.outputs:
                        que.append(("low",mod_object.name,t))
        else:  # incase the target is a conjunction
            mod_object.memory[origin] = signal # first updating the signal history from where it has received
            outgoing = "low" if all(x=="high" for x in mod_object.memory.values()) else "high"
            for t in mod_object.outputs:
                que.append((outgoing,mod_object.name,t))

print(low*high)
