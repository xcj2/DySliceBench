def get_int(): return int(input())
def get_float(): return float(input())
def get_line(): return input().split()
def get_lines(v): return [get_line() for _ in range(v)]
def get_int_line(): return list(map(int, get_line()))
def get_int_lines(v): return [get_int_line() for _ in range(v)]
def get_float_line(): return list(map(float, get_line()))
def get_float_lines(v): return [get_float_line() for _ in range(v)]

N, M = get_int_line()
X = get_int_line()

if (M <= N):
  print(0)
  exit(0)

X.sort()
x_dist = []
for i in range(M - 1):
  x_dist.append(X[i + 1] - X[i])
x_dist.sort()

sub = 0
for i in range(N - 1):
  sub += x_dist[-(i + 1)]

print(sum(x_dist) - sub)