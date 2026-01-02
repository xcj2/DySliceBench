import sys

def input():
    return sys.stdin.readline()[:-1]

from collections import defaultdict

N = int(input())
S = input()

def is_pos(n,S,N):
    dd = defaultdict(int)
    flag =True
    for i in range(N-n+1):
        s = dd[S[i:i+n]]
        if s!=0:
            if i+1-s>=n:
                flag=False
                break
        else:
            dd[S[i:i+n]]=i+1
    return flag


def bisect(i,j,S,N):
    while j-i>1:
        if is_pos((i+j)//2,S,N):
            j = (i+j)//2
        else:
            i = (i+j)//2
    return i

print(bisect(0,N//2 + 1, S, N))