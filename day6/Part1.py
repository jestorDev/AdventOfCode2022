
from enum import unique
import sys

def check_marker( candidate):
    uniques = set()
    for char in candidate:
        if char in uniques: return False
        uniques.add(char)
    return True
    

for line in sys.stdin:
    mark_len = 14
    for i in range(len(line) -mark_len +1):
        if check_marker( line[i : i+mark_len]): 
            print( "Ans :" , i+mark_len , " ", line[i : i+mark_len])
            break
        

print("--------------------")


