from time import time
from random import randrange
from bisect import bisect_left
import sys
def input():
	return sys.stdin.buffer.readline()[:-1]
start = time()
d = int(input())
c = list(map(int, input().split()))
C = sum(c)
s = [list(map(int, input().split())) for _ in range(d)]
#t = [int(input()) for _ in range(d)]
t = []
day = [[0] for _ in range(26)]
order = []

def score(t):
	res = 0
	minus = 0
	last = [0 for _ in range(26)]
	for i, x in enumerate(t):
		minus += C - c[x-1] * (i - last[x-1] + 1)
		res -= minus
		res += s[i][x-1]
		last[x-1] = i+1
		#print(res)
	return res

def tri(n):
	return n * (n-1) // 2

def change(i, to):
	diff = 0
	fr = t[i]-1
	#print(day[fr])
	#print(day[to])
	if fr == to:
		return 0
	fr_ind = bisect_left(day[fr], i+1)
	diff += (tri(day[fr][fr_ind] - day[fr][fr_ind-1]) + tri(day[fr][fr_ind+1] - day[fr][fr_ind])) * c[fr]
	diff -= (tri(day[fr][fr_ind+1] - day[fr][fr_ind-1])) * c[fr]
	diff -= s[i][fr]
	
	to_ind = bisect_left(day[to], i+1)
	diff += (tri(day[to][to_ind] - day[to][to_ind-1])) * c[to]
	diff -= (tri(day[to][to_ind] - (i+1)) + tri(i+1 - day[to][to_ind-1])) * c[to]
	diff += s[i][to]

	#if diff > 0:
	day[fr].pop(fr_ind)
	after = day[to][:to_ind] + [i+1] + day[to][to_ind:]
	day[to] = after
	t[i] = to+1
	#print("↓")
	#print(day[fr])
	#print(day[to])
	return diff
	#else:
		#return False

#score(t)
res = 0
minus = 0
last = [0 for _ in range(26)]
for i in range(d):
	minus += C
	#li = sorted(list(range(26)), key=lambda x: - c[x] * (i - last[x] + 1) - s[i][x])
	#order.append(li)
	#M_ind = li[0]
	M_ind = int(input())-1
	minus -= c[M_ind] * (i - last[M_ind] + 1)
	last[M_ind] = i+1
	res -= minus - s[i][M_ind]
	t.append(M_ind+1)
	day[M_ind].append(i+1)

for i in range(26):
	day[i].append(d+1)

#print(res)
#print(*t, sep="\n")
#print(score(t))
#print(*day, sep="\n")

for _ in range(int(input())):
	d, q = map(int, input().split())
	res += change(d-1, q-1)
	print(res)