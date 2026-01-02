from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())


def Base_10_to_n(X, n):

    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

N = int(input())

if N == 0:
	print(0)
	sys.exit()

ans = []
def calc(x):
	global ans

	if x%4 == 0:
		ans.append(0)
		ans.append(0)

	elif x%4 == 1:
		ans.append(1)
		ans.append(0)
		x -= 1
	elif x%4 == 2:
		ans.append(0)
		ans.append(1)
		x += 2
	elif x%4 == 3:
		ans.append(1)
		ans.append(1)
		x += 3

	return x//4

while N !=0:
	N = calc(N)


ans.reverse()
print(int(''.join(map(str,ans))))
