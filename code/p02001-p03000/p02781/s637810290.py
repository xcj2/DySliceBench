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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()
K = I()
S = str(N)

def calc1(S):
    if len(S)<1:
        return 0
    flag = False
    ans = 0
    for s in S:
        if flag:
            ans += 9
        else:
            if s!='0':
                flag = True
                ans += int(s)
    return ans

def calc2(S):
    bl = len(S)
    ans = 0
    if bl<2:
        return 0
    # 最上位bitに0
    ans += (bl-1)*(bl-2)*81 // 2
    # 最上位bitに1~(その数未満)
    ans += (int(S[0])-1)*9*(bl-1)
    # 最上位bitにその数
    val = -1
    for i in range(1,len(S)):
        if S[i]!='0':
            val = i
            break
    if val!=-1:
        newS = S[val:]
        ans += calc1(newS)
    return ans

def calc3(S):
    bl = len(S)
    if bl<3:
        return 0
    ans = 0
    # 最上位bitに0
    ans += (bl-1)*(bl-2)*(bl-3)*9*9*9 //6
    # 最上位bitに1~（その数未満）
    ans += (int(S[0])-1)*(bl-1)*(bl-2)*81 // 2
    # 最上位bitにその数
    val = -1
    for i in range(1,len(S)):
        if S[i]!='0':
            val = i
            break
    if val!=-1:
        newS = S[val:]
        ans += calc2(newS)
    return ans

if K==1:
    print(calc1(S))
if K==2:
    print(calc2(S))
if K==3:
    print(calc3(S))