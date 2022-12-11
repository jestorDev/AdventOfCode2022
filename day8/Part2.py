from cmath import sin
import enum
from json import tool
import sys

woods = []

for line in sys.stdin:
    if line != "\n":
        woods.append([ [int (x) , 0,0,0,0 ] for x in line.strip()])


def last_bigger(tree , since):
    for  i, tree_s in enumerate(list( reversed(since))):
        if tree_s >= tree[0]:
            return i+1
    return len(since)

def count_vis1 (order_woods, dir):
    for row in order_woods:
        elems_since = []
        for tree in  row:
            tree[dir] = last_bigger(tree , elems_since)         
            elems_since.append(tree[0])

def count_vis2 (order_woods, dir):
    for row in order_woods:
        elems_since = []
        for tree in reversed( row):
            tree[dir] = last_bigger(tree , elems_since)         
            elems_since.append(tree[0])




count_vis1 (woods, 1)
count_vis2 (woods, 2)
count_vis1 (list(zip(*woods)),3)
count_vis2 (list(zip(*woods)),4)

max_score= 0
for row in woods:
    for tree in  row:
        max_score = max( tree[1]*tree[2]*tree[3]*tree[4] , max_score)

print("total " , max_score)