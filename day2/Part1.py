
import sys
from unittest import result


#rock paper scisors
eqs  = {"X" : "A" , "Y" : "B", "Z" : "C"}

score_choice = {"X" : 1 , "Y" : 2, "Z" : 3}

score_result = {"L" :0 , "D" : 3, "W" : 6}

wins  = {"A" : "C" , "B" : "A"  , "C" : "B"}
 
score=  0

for line in sys.stdin:
    if line != "\n":
        oponent = line[0]
        me = eqs[line[2]]

        score += score_choice[line[2]]
        
        score += score_result ["D"] if oponent == me else 0
        score += score_result ["W"] if oponent == wins[me] else 0
        
print(score)
print("--------------------")
