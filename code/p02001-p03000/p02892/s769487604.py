import queue
import numpy as np
n = int(input())
class Node:
    def __init__(self):
        self.nextNode = []
        self.checkNgo = -1
        self.group = -1
        
Nodes = [Node() for i in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == '1':
            Nodes[i].nextNode.append(j)
            
def check(node,ngo):
    if node.checkNgo == -1:
        node.checkNgo = ngo
    elif node.checkNgo != ngo:
        return False
    elif node.checkNgo == ngo:
        return True
    for i in node.nextNode:
        if not check(Nodes[i],(ngo+1)%2):
            return False
    return True
    
def ngoCheck():
    stack = [Nodes[0]]
    Nodes[0].checkNgo = 0
    while stack:
        node = stack.pop()
        for i in node.nextNode:
            if Nodes[i].checkNgo != -1 and Nodes[i].checkNgo == node.checkNgo:
                return False
            if Nodes[i].checkNgo == -1:
                Nodes[i].checkNgo = (node.checkNgo+1)%2
                stack.append(Nodes[i])
    return True
    
if not check(Nodes[0],0):
    print(-1)
    exit(0)
    
def solv():
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if j in Nodes[i].nextNode:
                d[i][j] = 1
            else:
                d[i][j] = np.inf
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j] = d[i][k]+d[k][j]
    return d
    
def saidai(d):
    maxi = 0
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            maxi = max(maxi,d[i][j])
    return maxi
    
d = solv()
print(saidai(d)+1)