
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline




def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())

directions=np.array([[1,0],[0,1],[-1,0],[0,-1]])
directions = list(map(np.array, directions))

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact



def search(x,col_befedge):
    #print("top", x, count)
    global col

    k=1
    for n in adj[x]:
        
        e=tuple(sorted((n,x)))
        #print(e,k,col_befedge)
        if col[e]>0:
            continue
        if k==col_befedge:
            k+=1
        #if k==col_pa:
        #    k+=1
        
        col[e]=k
        search(n,k)
        k+=1
    
            
        

N=int(input())

adj=[[] for i in range(N+1)]

edges=[]
col={}
for i in range(N-1):
    tmp=acinput()
    adj[tmp[0]].append(tmp[1])
    
    adj[tmp[1]].append(tmp[0])
    col[tuple(sorted(tmp))]=0
    edges.append(tuple(sorted(tmp)))

    
#col=[-1]*(N+1)

#col[1]=1
#print(adj)

search(1,0)
#print(reduce(lambda a,b:max(a,b),col.keys))
#print(col)
print(max(col.values()))
#print(col[max(col)])
for se in edges:
    print(col[se])
