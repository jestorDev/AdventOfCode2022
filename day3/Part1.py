from os import PRIO_USER
import sys

total_priority= 0


def priority (item):
    ord_lower  = ord(item) - ord('a')   +1
    if ord_lower > 0 and ord_lower <= 26:
        return ord_lower
    ord_upper = ord(item) - ord('A')   +1 + 26
    return ord_upper

lines  = []

for line in sys.stdin:

    line = line.strip()
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    
    items1 =  set()

    for item in compartment1:
        items1.add(item)

    for item in compartment2:
        if item in items1:
            total_priority += priority(item)
            break
    


print("--------------------")
print ("max :" , total_priority)
