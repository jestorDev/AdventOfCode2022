
import sys

overlap_count = 0

def case1 (assignement1 , assignement2):
    return  assignement2[0]<=assignement1[0] and assignement1[1] <= assignement2[1]
def case2 (assignement1 , assignement2):
    return assignement1[0] <= assignement2[0] and assignement2[0]<=assignement1[1] and assignement1[1]<= assignement2[1]


for line in sys.stdin:
    if line != "\n":
        line= line.strip()
        assignemets =  line.split(",")
        assignement1 = list(map(int, assignemets[0].split("-")))
        assignement2 = list(map(int, assignemets[1].split("-")))
        if  case1 (assignement1 , assignement2) or case1 (assignement2 , assignement1) or  case2 (assignement1 , assignement2) or case2(assignement2 , assignement1):
            overlap_count +=1 
            print("A" , assignemets)
        


print("--------------------")
print ("count" , overlap_count)


#483  584 