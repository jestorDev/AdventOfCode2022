from ast import Str
from platform import node
import sys
from collections import deque

# --- SOS GPS --- 
# https://aoc.meilisearch.com/

class Node:
   def __init__(self, data):
      self.parent = None
      self.left = None
      self.right = None
      self.data = data

leafs = []

def setParents(root :Node , parent : Node):
    if root:
        root.parent = parent
        setParents(root.left , root)
        # Finally recur on right child
        setParents(root.right, root)

def printNodeTrail ( node  : Node ):
    act_node = node
    #if act_node: print("Trail of node : " , act_node.data)
    ans  = ""
    while act_node:
        #print( "> ", act_node.data)
        ans = act_node.data +ans
        act_node =  act_node.parent
    print(ans)
    return ans 




def levelOrder(root : Node ):
    if root is None :
        return

    toVisit = deque()
    toVisit.append((root , 0))
    
    while toVisit:
        (visit , level) = toVisit.popleft()
        if level == 11 and visit.left is None and visit.right  is None:
            printNodeTrail(visit)
        if visit.left:
            toVisit.append((visit.left , level +1))
        if visit.right:
            toVisit.append((visit.right, level+1))


def printTree(node : Node, level=0):
    global leafs
    if node != None:
        printTree(node.left, level + 1)
        #print(" "*level + node.data+ " " + str(level) + ("" if node.left or node.right else "+++"))

        if node.left is None and node.right is None:
            leafs.append(( node.data, level ))
        printTree(node.right, level + 1)

def idx_dismatch(sa,sb):
    for i , (ca,cb)  in enumerate( zip(sa,sb)):
        if ca != cb: return i
    return min (len(sa) , len(sb))

def match_generate( node :Node , residue : Str , level : int):

    if level > 50 :
        return 


    equals =idx_dismatch( node.data , residue)

    old_residue= node.data[equals:]

    if (old_residue != ""):
        new_node= Node(old_residue)
        new_node.left = node.left
        new_node.right = node.right

        if old_residue[0] == "L":
            node.left = new_node
            node.right = None
        else:
            node.right = new_node
            node.left = None
        node.data = node.data[:equals]


    new_residue =  residue[equals:]

    if len(new_residue) == 0 :
        return

    if  new_residue[0] == "L":
        if (node.left != None):
            match_generate(node.left , new_residue , level+1)
        else:
            node.left= Node(new_residue)
    if  new_residue[0] == "R":
        if (node.right != None):
            match_generate(node.right , new_residue , level+1)
        else:
            node.right= Node(new_residue)
    
    return node

root = Node("")

file1 = open('sorted', 'r')
while True:
    line = file1.readline().strip()
    if not line:
        break
    root = match_generate(root , line , 0)    
    
setParents(root , None)
#printTree(root)
levelOrder(root)
