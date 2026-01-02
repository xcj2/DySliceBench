import sys
from heapq import heapify, heappop
from operator import itemgetter

if sys.platform =='ios':
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

def main():
	N, M = MAP()
	A = MAP()
	BC = [MAP() for _ in range(M)]
	
	BC.sort(key= itemgetter(1), reverse=True)
	
	heapify(A)
	
	ans = 0
	
	fin = False
	for b, c in BC:
		#print(A, b, c)
		for _ in range(b):
			a = A[0]
			if a>c:
				fin = True
				break
			else:
				heappop(A)
				ans += c
				N -= 1
				if N == 0:
					fin = True
					break
		if fin:
			break
	
	print(ans+sum(A))

if __name__ == '__main__':
	main()