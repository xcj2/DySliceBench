def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()
N+=1

def naive_solver(N):
    output=[]
    for i in range(1,N):
        A=str(i)
        for j in range(1,N):
            B=str(j)
            if A[-1]==B[0] and B[-1]==A[0]:
#                 if A[0]=="1":
                output.append([A,B])
    return output

def naive_solver2(N):
    dicts={str(i):{str(j):0 for j in range(10)} for i in range(10) }
    for i in range(1,N):
        temp=str(i)
        dicts[temp[0]][temp[-1]] += 1
    return dicts

dicts = naive_solver2(N)

import itertools as it

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under



dicts = naive_solver2(N)

count = 0
for si in range(1,10):
    i=str(si)
    for sj in range(si,10):
        j = str(sj) 
        
#         count += dicts[i][j] * dicts[j][i] * 2
        if j!=i:
            count+=dicts[i][j] * dicts[j][i] * 2#2*cmb(dicts[i][j]+dicts[j][i],2)    
#             print(si,sj,dicts[i][j] * dicts[j][i] * 2)#2*cmb(dicts[i][j]+dicts[j][i],2))
        else:
            count+=dicts[i][j]*dicts[j][i]#cmb(dicts[i][j]+dicts[j][i],2)
#             print(si,sj,dicts[i][j]*dicts[j][i])

print(count)