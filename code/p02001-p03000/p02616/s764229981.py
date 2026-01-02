from collections import deque
import math

def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

def solve():
    n, k = NextInts()
    da = NextIntList()
    ans = 1
    MOD = 10**9+7
    
    if n == k:
        for i in range(n):
            ans = ans*da[i]%MOD
        return ans
    
    neg = []
    pos = []
    for i in range(n):
        if da[i] < 0:
            neg.append(da[i])
        else:
            pos.append(da[i])
    neg.sort()
    pos.sort()

    if len(pos) == 0 and k%2 == 1:
        neg.reverse()
        for i in range(k):
            ans = ans * neg[i] % MOD
        return ans
    
    pos.reverse()
    li = []
    po, ne = 0, 0
    if k%2 == 1:
        po = 1
        ans = pos[0]
    while po+1 < len(pos):
        li.append(pos[po]*pos[po+1])
        po += 2
    while ne+1 < len(neg):
        li.append(neg[ne]*neg[ne+1])
        ne += 2
    li.sort()
    li.reverse()
    for i in range(k//2):
        ans = li[i] * ans % MOD
    return ans

if __name__ == "__main__":
    print(solve())