import math
import sys
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

def isCycle(n,graph):

    in_degree=[0]*n

    for i in range(n):
        for j in graph[i]:
            in_degree[j]+=1

    queue=[]
    for i in range(len(in_degree)):
        if in_degree[i]==0:
            queue.append(i)

    counter=0

    while(queue):

        nu=queue.pop(0)

        for v in graph[nu]:
            in_degree[v]-=1

            if in_degree[v]==0:
                queue.append(v)
        counter+=1
    if counter==n:
        return False
    else:
        return True


if __name__=='__main__':

    V, E, = (int(x) for x in input().split())
    g = Graph(V)
    for i in range(E):
        v, e = (int(x) for x in input().split())
        g.addEdge(v,e)

    if(True == isCycle(g.V,g.graph)):
        print("1")
    else:
        print("0")

