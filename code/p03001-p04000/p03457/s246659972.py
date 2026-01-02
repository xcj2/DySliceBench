import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline()
def read(): return int(input())
def reads(): return [int(i) for i in input().split()]

def f(dt, dx, dy):
	if dt == dx + dy:
		return True
	elif dt < dx + dy:
		return False
	else:
		return f(dt-2, dx, dy)

N = read()
t, x, y = [0]*(N+1), [0]*(N+1), [0]*(N+1)
for i in range(1, N+1):
	t[i], x[i], y[i] = reads()

ans = True
for i in range(N):
	dt = t[i+1] - t[i]
	dx = abs(x[i+1] - x[i])
	dy = abs(y[i+1] - y[i])
	ans = ans and f(dt, dx, dy)

if ans:
	print('Yes')
else:
	print('No')