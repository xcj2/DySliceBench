def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort(reverse = True)
    return divisors

import heapq
#from collections import deque
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
#mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N, K = LI()
A = LI()
cou = int(0)
sumA = sum(A)
anscandi = make_divisors(sumA)
#print(anscandi)

for i in anscandi:
    Smod = int(0)
    que = []
    for j in range(N):
        que.append((A[j] % i) *(-1))
        Smod += A[j] % i
    need = Smod//i
    heapq.heapify(que)
    for _ in range(need):
        heapq.heappop(que) * (-1)
    if K>=(sum(que)*(-1)):
        ans = i
        break


print(ans)
