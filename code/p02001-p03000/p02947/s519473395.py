import sys
import numpy as np
from collections import Counter

if sys.platform =='ios':
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]


from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = INT()
S = [[s for s in input().strip()] for _ in range(N)]

words = []
for s in S:
	s.sort()
	words.append(s)

words.sort()

ans = []
tmp = ''
num = -1
for w in words:
	#print(tmp , w, num)
	if tmp == w:
		#print('same')
		ans[num] += 1
		#print(ans)
	else:
		#print('different')
		tmp = w
		num+=1
		ans.append(1)
		#print(ans)
		
#print(ans)

count = 0
for a in ans:
	if a != 1: count += cmb(a, 2)

print(count)