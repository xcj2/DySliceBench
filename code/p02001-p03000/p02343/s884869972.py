#coding:utf-8
import time

N,Q = map(int,input().split())
rank = [0 for i in range(N)]

class Tree:
    def __init__(self,par,key):
        self.par = par
        self.key = key

List = [Tree(i,i) for i in range(N)]

def unit(x,y):
    while List[x].par != x:
        x = List[x].par
    a = rank[x]
            
    while List[y].par != y:
        y = List[y].par
    b = rank[y]
    if a <= b:
        if a == b:
            rank[x] += 1
        List[y].par = x
    else:
        List[x].par = y



def Find(x,y):
    Q = []
    P = []
    while List[x].par != x:
        x = List[x].par
        Q.append(x)
            
    while List[y].par != y:
        y = List[y].par
        P.append(y)
    for xi in Q:
        List[xi].par = x
        rank[xi] = 1
    for yi in P:
        List[yi].par = y
        rank[yi] = 1
    if x == y:
        print(1)
    else:
        print(0)
    
        
for i in range(Q):
    com, x,y = map(int,input().split())

    if com == 0:
        unit(x,y)
            
    else:
        Find(x,y)



