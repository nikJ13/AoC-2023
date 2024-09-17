# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:55:13 2023

@author: niket
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:25:51 2023

@author: niket
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:01:50 2023

@author: niket
"""

from collections import defaultdict


def removeSeedHeading(text):
    return text.split(': ')[1]

def extractSeeds(Lines):
    seeds_str = removeSeedHeading(Lines[0].strip())
    seeds_list = seeds_str.split()
    for seed in seeds_list:
        dict_seeds[int(seed)] = int(seed)
    return

def extract(text,hashmap_source):
    destination_start, source_start, range_val = int(text.strip().split()[0]),int(text.strip().split()[1]),int(text.strip().split()[2])
    for element in hashmap_source:
        if element >= source_start and element <= source_start+range_val:
            diff = element - source_start
            hashmap_source[element] = destination_start + diff
    return

def populate(hashmap_source,hashmap_destination):
    for element in hashmap_source:
        hashmap_destination[hashmap_source[element]] = hashmap_source[element]
    return

def populateList(hashmap_source, destination_list):
    for element in hashmap_source:
        destination_list.append(element)
    return
            

dict_seeds = defaultdict(int)
dict_soil = defaultdict(int)
dict_fertilizer = defaultdict(int)
dict_water = defaultdict(int)
dict_light = defaultdict(int)
dict_temp = defaultdict(int)
dict_humid = defaultdict(int)
loc = []
file1 = open('input5.txt')
Lines = file1.readlines()
extractSeeds(Lines)
line_counter = 1
n = len(Lines)
while line_counter<n:
    Lines[line_counter] = Lines[line_counter].strip()
    print(Lines[line_counter])
    if Lines[line_counter]=='':
        line_counter+=1
        continue
    elif Lines[line_counter]=='seed-to-soil map:':
        line_counter += 1
        while Lines[line_counter]!='\n':
            #print('first')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_seeds)
            line_counter += 1
        populate(dict_seeds, dict_soil)
        print(dict_seeds)
        print(dict_soil)
    elif Lines[line_counter]=='soil-to-fertilizer map:':
        line_counter += 1
        while Lines[line_counter]!='\n':
            #print('second')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_soil)
            line_counter += 1
        populate(dict_soil, dict_fertilizer)
        print(dict_fertilizer)
    elif Lines[line_counter]=='fertilizer-to-water map:':
        line_counter += 1
        while Lines[line_counter]!='\n':
            #print('third')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_fertilizer)
            line_counter += 1
        populate(dict_fertilizer, dict_water)
        print(dict_water)
    elif Lines[line_counter]=='water-to-light map:':
        line_counter += 1
        while Lines[line_counter]!='\n':
            #print('fourth')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_water)
            line_counter += 1
        populate(dict_water, dict_light)
        print(dict_light)
    elif Lines[line_counter]=='light-to-temperature map:':
        line_counter += 1
        while Lines[line_counter]!='\n':
            #print('fifth')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_light)
            line_counter += 1
        populate(dict_light, dict_temp)
        print(dict_temp)
    elif Lines[line_counter]=='temperature-to-humidity map:':
        line_counter += 1
        while Lines[line_counter]!='\n':
            #print('sixth')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_temp)
            line_counter += 1
        populate(dict_temp, dict_humid)
        print(dict_humid)
    elif Lines[line_counter]=='humidity-to-location map:':
        line_counter += 1
        while line_counter<n and Lines[line_counter]!='\n':
            #print('seventh')
            #print(Lines[line_counter])
            extract(Lines[line_counter],dict_humid)
            line_counter += 1
        populateList(dict_humid, loc)
        print(loc)
    line_counter += 1

print(sorted(loc)[0])