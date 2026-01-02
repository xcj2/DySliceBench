import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline()
def read(): return int(input())
def reads(): return [int(i) for i in input().split()]
	
from operator import itemgetter

N, H = reads()
ab = [None]*N
for i in range(N):
	ab[i] = tuple(reads())
	
ab.sort(key=itemgetter(1), reverse=True)

a_max = 0
b_of_a_max = 0
a_max_index = 0
for i in range(N):
	if ab[i][0] >= a_max:
		a_max = ab[i][0]
		b_of_a_max = ab[i][1]
		a_max_index = i
del ab[a_max_index]
	
ans = 0

for i in range(N-1):
	if b_of_a_max > H:
		H = 0
		ans += 1
		break
	if ab[i][1] >= a_max:
		H -= ab[i][1]
		ans += 1
		if H <= 0:
			break
	else:
		break
		
if H > 0 and b_of_a_max > a_max:
	H -= b_of_a_max
	ans += 1
	
if H > 0:
	ans += -(-H // a_max)
	
print(ans)
