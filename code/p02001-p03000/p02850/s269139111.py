import sys,math

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	N = II()
	to = [[] for _ in range(N)]
	ans = {}
	order = []
	for i in range(N-1):
		a,b = MI()
		a -= 1;b -= 1
		ans[str(a)+"-"+str(b)] = 0
		order.append(str(a)+"-"+str(b))
		to[a].append(b);to[b].append(a)
	
	def bfs():
		from collections import deque
		hist = [True]*N
		que = deque()
		que.append(0)
		e_colors = [0]*N
		max_c = 0
		while len(que) > 0:
			n = que.popleft()
			hist[n]=False
			for i in to[n]:
				if(hist[i]):
					ch = e_colors[n] | e_colors[i]
					index = int(math.log2(~ch & -~ch))
					e_colors[n] += 1 << index
					e_colors[i] += 1 << index
					ans[str(min(n,i))+"-"+str(max(n,i))] = index+1
					if(max_c < index+1): max_c = index+1
					que.append(i)
		print(max_c)
		for i in order:
			print(ans[i])

	bfs()


main()