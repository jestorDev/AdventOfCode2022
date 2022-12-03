from os import PRIO_USER
import sys

total_priority= 0

def priority (item):
    ord_lower  = ord(item) - ord('a') + 1
    if ord_lower > 0 and ord_lower <= 26:
        return ord_lower
    ord_upper = ord(item) - ord('A') + 1 + 26
    return ord_upper

lines  = []
i = 0 
for line in sys.stdin:
    i +=  1    

    if  i%3 ==1 :
        lines  = []

    lines.append(line.strip())

    if  i%3 ==0 :
        print(lines)
        items1 =  set()
        for item in lines[0]:
            items1.add(item)
        items12 =  set()

        for item in lines[1]:
            if item in items1:
                items12.add(item)

        print (items1)
        print (items12)
        for item in lines[2]:
            if item in items12 :
                total_priority += priority(item)
                break

print("--------------------")
print (total_priority)
