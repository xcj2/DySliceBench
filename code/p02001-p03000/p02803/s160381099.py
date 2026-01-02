import sys,copy

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def IS(): return sys.stdin.readline()
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	H,W = MI()
	maze = [[-1 for _ in range(W)] for _ in range(H)]
	for i in range(H):
		S = IS()
		for j,s in enumerate(S):
			if s == '#':
				maze[i][j] = '#'

	def bfs(sx,sy):
		from collections import deque
		que = deque()
		dist_map = copy.deepcopy(maze)
		dist_map[sy][sx]=0
		que.append((sx,sy))
		res = 0
		while len(que) > 0:
			x,y=que.popleft()
			for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
				nx = x+dx
				ny = y+dy
				if(0<=nx<W and 0<=ny<H):
					if(dist_map[ny][nx]==-1):
						dist_map[ny][nx] = dist_map[y][x]+1
						res = max(res, dist_map[ny][nx])
						que.append((nx,ny))
		return res

	ans = -1
	for i in range(H):
		for j in range(W):
			if(maze[i][j]==-1):
				dist = bfs(j,i)
				if(dist > ans):
					ans = dist
	print(ans)

main()