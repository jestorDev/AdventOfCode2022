from ast import Str
from platform import node
import sys



class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data



leafs = []
def printTree(node : Node, level=0):
    global leafs
    if node != None:
        printTree(node.left, level + 1)
        print(" "*level + node.data+ " " + str(level) + ("" if node.left or node.right else "+++"))

        if node.left is None and node.right is None:
            leafs.append(( node.data, level ))
        printTree(node.right, level + 1)


def minimumDepth(root :Node, level):
    if (root == None):
        if (level == 11):
            print("o")
        return (  "", level)
 
    level += 1
     
    minl =minimumDepth(root.left, level)
    minr = minimumDepth(root.right, level)
    if minl[1] <= minr[1]:
        return (root.data  + minl[0] , minl[1] ) 
    else:
        return (root.data  + minr[0] , minr[1] ) 



def idx_dismatch(sa,sb):
    for i , (ca,cb)  in enumerate( zip(sa,sb)):
        if ca != cb: return i
    return min (len(sa) , len(sb))


def match_generate( node :Node , residue : Str , level : int):

    if level > 20 :
        return 


    
    #print("+++++++++++++++++++++++")
    #print("node :" , node.data)
    #print("res :" , residue)
    #print("+++++++++++++++++++++++")
    

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
    
printTree(root)
#print (leafs)
#print ( minimumDepth(root , 0))
#print(min(leafs, key = lambda t: t[1]))
#%%


# gertrudis