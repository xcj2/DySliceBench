from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N,K = inpl()
A = []
for i in range(N):
    a = int(input())
    A.append(a)

a_max = 300001

UNITE = 0
N0 = 2**(a_max-1).bit_length()
data = [UNITE]*(2*N0)
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = max(data[2*k+1], data[2*k+2])
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = UNITE
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])

        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

for a in A:
    segmax = query(max(0,a-K),min(a_max,a+K)+1)
    update(a,segmax+1)

print(max(data))