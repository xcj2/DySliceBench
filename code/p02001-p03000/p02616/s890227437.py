import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N,K = LI()
A = LI()

if K == N:
    ans = 1
    for i in range(N):
        ans *= A[i]
        ans %= mod
    print(ans)
    exit()

plus = []
minus = []
zeros = []

for i in range(N):
    if A[i] > 0:
        plus.append(A[i])
    elif A[i] < 0:
        minus.append(-A[i])
    else:
        zeros.append(A[i])

plus.sort(reverse=True)
minus.sort(reverse=True)

if len(plus):
    if K%2:
        ans = plus[0]
        p_place = 1
        m_place = 0
        K -= 1
    else:
        ans = 1
        p_place = 0
        m_place = 0
    while K:
        val1 = plus[p_place]*plus[p_place+1] if p_place <= len(plus)-2 else -float('inf')
        val2 = minus[m_place]*minus[m_place+1] if m_place <= len(minus)-2 else -float('inf')
        if val1 == val2 == -float('inf'):
            if p_place == len(plus)-1:
                ans *= plus[p_place]
                ans %= mod
                K -= 1
            if K:
                print(0)
                exit()
        else:
            K -= 2
            if val1 == -float('inf'):
                ans *= val2
                ans %= mod
                m_place += 2
            elif val2 == -float('inf'):
                ans *= val1
                ans %= mod
                p_place += 2
            elif val1 >= val2:
                ans *= val1
                ans %= mod
                p_place += 2
            else:
                ans *= val2
                ans %= mod
                m_place += 2
    print(ans)
else:
    if K%2:
        if len(zeros):
            print(0)
        else:
            ans = 1
            for i in range(K):
                ans *= -minus[len(minus)-1-i]
                ans %= mod
            print(ans)
    else:
        m_place = 0
        ans = 1
        while K:
            if m_place <= len(minus)-2:
                ans *= minus[m_place]*minus[m_place+1]
                ans %= mod
                m_place += 2
                K -= 2
            else:
                print(0)
                exit()
        print(ans)