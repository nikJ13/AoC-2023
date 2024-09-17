# each module that broadcasts signals is stored as objects, containing information such as name, type, output and memory
import sys
import math

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

counter = 0
ans = 0

(feed,) = [name for name,mod in modules.items() if "rx" in mod.outputs] # which module sends signal to rx


cycle_lengths = {}

visited = {name:0 for name,mod in modules.items() if feed in mod.outputs} # get the parents of the feed (which is in turn connected to rx)

#print(cycle_lengths)
#sys.exit(0)

# assumption #1: conjunction module is connected to rx always (for all usecases)
# assumption #2: since the conjunction module is connected, all its parent signals have to be low for it to send
#       a low signal to rx (this condition is given in the question). Hence, the assumption made is that the parents of
#       this conjunction module follow a cycle for emitting low sginals. Hence, the LCM of both (or more) of the cycle
#       lengths will give the answer

while True:
    counter += 1
    #signal,origin,target
    que = [("low","broadcaster",y) for y in broadcaster_destinations]
    #print(que.pop(0))
    while que:
        #print(que)
        signal,origin,target = que.pop(0)
        
        if target not in modules:
            continue
        
        mod_object = modules[target] # destination where the signal is going
        
        # a low signal is passed after mutiple highs (or it can be passed before any high)
        # hence, it is essential to keep track when the parents of the feed get a high
        
        #another assumption is that a low will come once the parents receive a high
        
        #here, the if condition checks if a parent of the feed is passing high signal to it or not
        if mod_object.name==feed and signal=="high":
            visited[origin] += 1
            
            if origin not in cycle_lengths: # here, we catch the first time a parent gets a high signal and store it 
                cycle_lengths[origin] = counter  # this value does not changes as we need to find the min number of times the button is pressed
            # else:
            #     assert counter == visited[origin] * cycle_lengths[origin]
                
            if all(visited.values()): #checking if all the parents of feed have been visited
            #calculating the lcm
                temp = 1
                for length in cycle_lengths.values():
                    temp = math.lcm(temp,length)
                print(temp)
                sys.exit(0)
        
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
    if ans!=0:
        break

#print(ans)