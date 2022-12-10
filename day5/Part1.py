
from pickle import BINFLOAT
import sys

is_second_half = False


tower = []


def exec_order (order , htower):
    to_move = htower[order[1]][-(order[0]+1):]

    htower[order[1]]  =  htower[order[1]][:-(order[0]+1)]
    
    htower[order[2]].extend(reversed( to_move))
    #print('-----')
    #print(to_move)
    #print('---------------')
    #for  f in htower :
        #print(f)
    
    return 

def horizontal_tower (tower):


    htower  =  [ [] for _ in range (len(tower[0]))]
    for floor in reversed(tower):
        for i, block in enumerate(floor):
            if block != "": htower[i].append(block)

    return htower

for line in sys.stdin:

    if line != "\n" and not is_second_half:

        blocks = [line[i:i+4].strip() for i in range(0, len(line), 4)]
        
        if blocks[0] != "1":
            tower.append(blocks)
        
    if line != "\n" and is_second_half:
        
        line = line.replace('move', '')
        line = line.replace('from', '')
        line = line.replace('to', '')
        order = line.split()
        order = [ int (o) -1 for o  in order]
        
        exec_order( order, htower )

        #print(order)

    if line == "\n":
        is_second_half = True
        htower = horizontal_tower( tower)


print("--------Message------------")
for c in htower:
    print (c[len(c)-1])


