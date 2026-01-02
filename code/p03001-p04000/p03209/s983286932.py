
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

N,X=acinput()

n=[0]*(N+1)
n[0]=1
for i in range(1,N+1):
    n[i]=n[i-1]*2+3
    
    
p = [0]*(N+1)
p[0] = 1
for i in range(1, N+1):
    p[i] = p[i-1]*2+1

def f(N,k):
    
        
    if N == 0 and k>=1:
        return 1
    
    if k <= 1:
        return 0
    
    if k<=n[N-1]+1:
        return f(N-1,k-1)
    else:
        r=k-n[N-1]-2
        return p[N-1]+f(N-1,r)+1


print(f(N,X))