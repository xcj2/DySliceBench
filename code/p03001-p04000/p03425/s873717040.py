import sys
from operator import mul
from functools import reduce

if sys.platform =='ios':
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

MARCH = 'MARCH'
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = INT()
S = [input().rstrip() for _ in range(N)]

S = [s for s in S if s[0] in MARCH]

A = [0]*5
for s in S:
	A[MARCH.index(s[0])] += 1

#print(A)

if sum(A) < 3:
	print(0)
	sys.exit()

ans = cmb(sum(A), 3)
#print(ans)

for a in A:
	if a<=1:continue
	if a>=3:
		ans -= cmb(a, 3)
	ans -= cmb(a, 2) * (sum(A)-a)

print(ans)