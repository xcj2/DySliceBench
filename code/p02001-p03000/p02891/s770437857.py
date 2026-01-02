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

S = str(input())
n = len(S)
K = I()

num = 0
flag = False
for i in range(1,n):
    if S[i]==S[i-1] and flag==False:
        num += 1
        flag = True
    else:
        flag = False

if flag==False and S[0]==S[-1]:
    num2 = 1
    flag2 = False
    for i in range(2,n):
        if S[i]==S[i-1] and flag2==False:
            num2 += 1
            flag2 = True
        else:
            flag2 = False
    if n==1:
        flag2 = True
    if flag2==False:
        print(num+num2*(K-1))
        exit()
    else:
        print(num2*(K//2) + num*(K-K//2))
        exit()
else:
    print(num*K)