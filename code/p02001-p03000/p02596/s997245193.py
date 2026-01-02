import sys
from math import sqrt, gcd, ceil, log
# from bisect import bisect, bisect_left
from collections import defaultdict, Counter, deque
# from heapq import heapify, heappush, heappop
input = sys.stdin.readline
read = lambda: list(map(int, input().strip().split()))

# sys.setrecursionlimit(5*10**6)

def f(n):
	i = 0
	while n%10 == 7:
		n //= 10
		i += 1
	return((n,i))
def f2(a, b):
	return(b + [0, 10][a > b] - a)
def main():
	n = int(input()); 
	dic = defaultdict(int)
	for i in range(1, 10):
		for j in (1, 3, 7, 9):
			dic[(j, (i*j)%10)] = i
	# print(dic)
	if n%10 in (1, 3, 7, 9):
		t = n%10; ans = 0
		m, ans = f(n*(dic[(t, n%10)]))
		# print(m, ans)
		while m != 0:
			# print(m, f2(m%10, 7), n*dic[(t, f2(m%10, 7))])
			m += n*dic[(t, f2(m%10, 7))]
			# print(m)

			# print(m, "1")
			m, y = f(m)
			# print(m, y, "2")
			ans += y
		print(ans)



	else:print(-1)
	# print(f2(8, 9))





if __name__ == "__main__":
	main()