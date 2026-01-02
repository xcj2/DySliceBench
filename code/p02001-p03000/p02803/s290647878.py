from sys import stdin
# stdin = open("testdata.txt", "r")

def input():
	return stdin.readline().strip()

from collections import defaultdict, deque

R, C = map(int, input().split())

grid = [None]*R

for i in range(R):
	temp = input()
	grid[i] = temp

def get_neighs(r, c):
	is_valid = lambda x, y: 0 <= x < R and 0 <= y < C and grid[x][y]=='.'
	dr = [-1, 0, 1, 0]
	dc = [0, 1, 0, -1]
	return [(r+dr[i], c+dc[i]) for i in range(4) if is_valid(r+dr[i], c+dc[i])]


def get_max(r0, c0):
	visited = {(r0, c0),}
	dq = deque()
	dq.append((r0, c0, 0))
	max_steps = 0
	while dq:
		r, c, steps = dq.popleft()
		max_steps = max(max_steps, steps)
		for _r, _c in get_neighs(r, c):
			if (_r, _c) not in visited:
				dq.append((_r, _c, steps+1))
				visited.add((_r, _c))
	return max_steps

ans = 0
for r in range(R):
	for c in range(C):
		if grid[r][c]=='.':
			ans = max(get_max(r, c), ans)
print(ans)