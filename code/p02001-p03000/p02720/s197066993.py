import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

def DFS(N, string, val, L):
	L.append(int(string))
	if N == 11:
		return
	else:
		if val == 0:
			DFS(N + 1, string + "0", 0, L)
			DFS(N + 1, string + "1", 1, L)
		elif val == 9:
			DFS(N + 1, string + "9", 9, L)
			DFS(N + 1, string + "8", 8, L)
		else:
			DFS(N + 1, string + str(val + 1), val + 1, L)
			DFS(N + 1, string + str(val), val, L)
			DFS(N + 1, string + str(val - 1), val - 1, L)

#処理内容
def main():
	K = int(input())
	L = []
	for i in range(10):
		DFS(0, str(i), i, L)

	L = sorted(list(set(L)))

	print(L[K])


if __name__ == '__main__':
	main()