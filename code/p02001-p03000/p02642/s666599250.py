
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def array(size,init=0):
    return [[init for j in range(size[1])] for i in range(size[0])]



def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact


def permutate(x,A):
    n=len(x)
    res=[-1]*n
    for i in range(n):

        res[i]=x[A[i]]
    return res


def generate_bin(digit):
    for b in range(2**digit):
        b=bin(b)
        tmp=b[2:].zfill(digit)
        yield list(map(int,tmp))
        #b=list(map(int,list(b[2:].zfill(digit))))
        #yield b
        

def search(x, count):
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
A=acinput()


M=max(A)
m=[0]*(M+1)
for i in range(N):
    
    x=A[i]
    m[x]+=1
    
    k=2
    while True:
        if x*k<=M:
            m[x*k]+=1
        
            k+=1
        else:
            break


res=0
for a in A:
    if m[a]==1:
        res+=1

        
print(res)
        
        
#print(m)