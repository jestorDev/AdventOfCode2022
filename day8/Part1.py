from json import tool
import sys

woods = []

for line in sys.stdin:
    if line != "\n":
        woods.append([ [int (x) , False ] for x in line.strip()])



def count_vis1 (order_woods):
    n_visible  = 0
    for row in order_woods:
        last_max = -1
        for tree in row:
            if tree[0] > last_max:
                last_max = tree[0]
                if tree[1] == False:
                    n_visible +=1
                    tree[1] =True
    return n_visible


def count_vis2 (order_woods):
    n_visible  = 0
    for row in order_woods:
        last_max = -1
        for tree in reversed( row):
            if tree[0] > last_max:
                last_max = tree[0]
                if tree[1] == False:
                    n_visible +=1
                    tree[1] =True
    return n_visible

total =count_vis1 (woods) + count_vis2 (woods) + count_vis1 (list(zip(*woods))) + count_vis2 (list(zip(*woods)))



print("-------------------------" )
print("total " , total)