n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def factorial(x):
	ans = 1
	for i in range(2, x+1):
		ans *= i
	return ans
	
def order(P):
	ranks = []
	used = [False] * (n+1)
	for i in range(n):
		c = P[i]
		j = 1
		rank = 0
		while j <= c:
			if not used[j]:
				rank += 1
			j += 1
		used[c] = True
		ranks.append(rank)
	return rank2order(ranks)
	
def rank2order(ranks):
	ng = factorial(n)
	order = 1
	for i in range(n-1):
		ng = ng // (n-i)
		order += ng*(ranks[i]-1)
	return order


a = order(P)
b = order(Q)
print (abs(a-b))