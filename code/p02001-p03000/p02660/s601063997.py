import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#篩
num = 10 ** 6 + 1 #適当に値を入れる
L = [1 for i in range(num)]; L[0] = 0; L[1] = 0
plist = []
for i in range(num):
	if L[i] == 1:
		plist.append(i); c = 2
		while i * c <= num - 1:
			L[i * c] = 0; c += 1

def prime_factorization(N):
	D = defaultdict(int)
	for i in plist:
		while N % i == 0:
			D[i] += 1; N = int(N // i)

	if N != 1:
		D[N] += 1

	return D


#処理内容
def main():
	N = int(input())
	fac = prime_factorization(N)
	ans = 0
	# print(fac)
	for i in fac:
		for j in range(1, 100):
			if fac[i] < int((j * (j + 1) // 2)):
				ans += j - 1
				break

	print(ans)

if __name__ == '__main__':
	main()