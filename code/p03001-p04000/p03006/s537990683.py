
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



def serch(x, count):
    #print("top", x, count)
            

    for d in directions:
        nx = d+x
        #print(nx)
        if np.all(0 <= nx) and np.all(nx < (H, W)):
            if field[nx[0]][nx[1]] == "E":
                count += 1 
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)  
                continue
            if field[nx[0]][nx[1]] == "#":
                field[nx[0]][nx[1]] = "V"
                count = serch(nx, count)    
                 
    return count

N=int(input())

x= [np.array(acinput())for i in range(N)]
#x = [acinput() for i in range(N)]
#print(tmp)
#x=sorted(tmp)

import itertools as it

from collections import defaultdict
#es=10**10

#dc={}
dc=defaultdict(int)

for cb in it.combinations(x,2):
    d=cb[0]-cb[1]
    d2=tuple(-d)
    d=tuple(d)
    dc[d]+=1
    dc[d2]+=1

#print(dc)    
if N==1:
    print(1)
else:
    print(N-max(dc.values()))
    
    
