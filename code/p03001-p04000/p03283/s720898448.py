
import numpy as np
import sys
sys.setrecursionlimit(100000)



def acinput():
    return list(map(int, input().split(" ")))



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

N,M,Q=acinput()

A=np.zeros([N+1,N+1])

for i in range(M):
    tmp=acinput()
    A[tmp[0],tmp[1]]+=1
Acs=np.cumsum(A,axis=1 )
Acs=np.cumsum(Acs,axis=0)

for i in range(Q):
    tmp=acinput()
    print(int(Acs[tmp[1], tmp[1]]-Acs[tmp[1],tmp[0]-1]-Acs[tmp[0]-1,tmp[1]]+Acs[tmp[0]-1, tmp[0]-1]))
