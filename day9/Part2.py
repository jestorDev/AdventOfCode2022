
import sys


H_pos = [0,0]
Tails = [[0,0] for _ in range (9)]

table  = [ [ "0" for x in range( 6) ] for y in range (6)]

visited = set()

def sum_l (a,b):
    return [ai + bi  for ai,bi in zip(a, b)]

def neg (a):
    return [ - ai  for ai in a]

def update_t (H_pos , T_pos ):
    dif = sum_l(H_pos , neg(T_pos))
    updir= [0 ,0]

    if any( abs (d) ==2 for d in dif ):
        for i , d in enumerate(dif) :
            updir[i] = d//2 if abs (d) == 2 else d
    
    nt_pos =  sum_l(T_pos , updir)

    #table[nt_pos[1]] [nt_pos[0] ] = "T"
    #table[H_pos[1]] [H_pos[0] ] = "H"
    #print("----------------"   )
    #print("T  : "  ,T_pos )
    #print("H  : "  ,H_pos )
    #print("H  : "  ,dif )
    #print("Updating  : "  ,nt_pos )
    #for r in reversed(table) :
    #    print(r)
    

    return  nt_pos

dirs = { "U" : [0,1],"R" : [1,0],"D" : [0,-1],"L" : [-1,0],}
for line in sys.stdin:
    if line != "\n":
        order = line.split()
        dir  = dirs[order[0]]
        steps  = int(order[1])
        for _ in range (steps):
            H_pos = sum_l(H_pos , dir)
            Tails[0] = update_t (H_pos , Tails[0] )
            for i in range(8):
                Tails[i+1] = update_t (Tails[i] , Tails[i+1] )

            visited.add(tuple(Tails[8]))






print("--------------------")
print ("visited :" , visited)
print ("visited :" , len(visited))


