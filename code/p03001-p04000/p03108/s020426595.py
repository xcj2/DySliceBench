N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]
root = [i for i in range(N+1)]
comp_size = [1] * (N+1)

def find_root(x):
    a = root[x]
    if a == x:
        return x
    y = find_root(a)
    root[x] = y
    return y

def find_root(x):
  y = root[x]
  if x == y:
    return x
  z = find_root(y)
  root[x] = z
  return z

def merge(x, y):
    rx = find_root(x)
    ry = find_root(y)
    if rx == ry:
        return 0
    sx = comp_size[rx]
    sy = comp_size[ry]
    if sx >= sy:
        root[ry] = rx
        comp_size[rx] += sy
    else:
        root[rx] = ry
        comp_size[ry] += sx
    return sx * sy

result = N * (N-1) // 2
answer = []
for x, y in edges[::-1]:
    answer.append(result)
    result -= merge(x, y)

for r in answer[::-1]:
    print(r)
