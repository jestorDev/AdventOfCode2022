
from re import A
import sys
sys.setrecursionlimit(1500)

total = 0 

structure = {}
parent = {"//":""}
weigths = {}
actual= ""

for line in sys.stdin:
    if line != "\n":
  
        comand = line.split()
        if "cd" == comand[1]:
            if  ".." == comand[2]:
                actual =  actual [:actual[:-1].rfind('/')+1]
            else:
                actual +=   comand[2]+"/"

        if "dir" == comand[0]:
            if  actual not in structure:
                structure[actual] = {}
            structure[actual][actual +comand[1]+ "/"] = 0
            
            parent[comand[1]] = actual

        if comand[0].isnumeric() : 
            if  actual not in structure:
                structure[actual] = {}
            structure[actual][actual + comand[1]] = int (comand[0])


        #print("------------------------")
        #print(line)
        #print(actual)
        #print(structure)
        #print(parent) 


def fill_f_weigths( folder , structure):
    #print("Visit " ,folder)
    total = 0
    for elem in structure[folder]:
        if structure[folder][elem] == 0:
            structure[folder][elem] = fill_f_weigths( elem , structure)
            if elem not in weigths:
                weigths[elem] = structure[folder][elem]

        total += structure[folder][elem]

    return total
            

#czvcf






print("--------------------")

print("--------------------")
print(structure)
weigths["//"]  = fill_f_weigths( "//" , structure)
print ("total :" , weigths["//"])
print("--------------------")
print(weigths)


suma = 0
for folder in weigths:
    if weigths[folder] <= 100000:
        suma +=weigths[folder]

print("suma: " , suma)