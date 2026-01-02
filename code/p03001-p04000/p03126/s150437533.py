def get_int(): return int(input())
def get_float(): return float(input())
def get_line(): return input().split()
def get_lines(v): return [get_line() for _ in range(v)]
def get_int_line(): return list(map(int, get_line()))
def get_int_lines(v): return [get_int_line() for _ in range(v)]
def get_float_line(): return list(map(float, get_line()))
def get_float_lines(v): return [get_float_line() for _ in range(v)]

N, M = get_int_line()
K = get_int_lines(N)

for i in range(N):
  K[i].remove(K[i][0])

ans = 0
for i in range(M):
  f = True
  for j in range(N):
    ff = len([v for v in K[j] if v == i + 1]) > 0
    if (not ff):
      f = False
  if (f): ans += 1

print(ans)