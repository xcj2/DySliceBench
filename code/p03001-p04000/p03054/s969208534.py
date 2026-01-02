import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

H,W,N = II()
sr,sc = II()
S = str(input())
T = str(input())

for i in range(N)[::-1]:
    if i==N-1:
        l = 1+(int(S[i]=='L'))
        r = W-(int(S[i]=='R'))
        u = 1+(int(S[i]=='U'))
        d = H-(int(S[i]=='D'))
    else:
        l = max(l+int(S[i]=='L')-int(T[i]=='R'), 1+(int(S[i]=='L')))
        r = min(r-int(S[i]=='R')+int(T[i]=='L'), W-(int(S[i]=='R')))
        u = max(u+int(S[i]=='U')-int(T[i]=='D'), 1+(int(S[i]=='U')))
        d = min(d-int(S[i]=='D')+int(T[i]=='U'), H-(int(S[i]=='D')))
    if l>r or u>d:
        print('NO')
        exit()

if l<=sc<=r and u<=sr<=d:
    print('YES')
else:
    print('NO')