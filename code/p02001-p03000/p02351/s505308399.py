import sys
readline = sys.stdin.readline
write = sys.stdout.write
N, Q = map(int, readline().split())

data0 = [0]*(N+1)
data1 = [0]*(N+1)
def _add(data, k, x):
    while k <= N:
        data[k] += x
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1))
    _add(data0, r, x*(r-1))
    _add(data1, l, x)
    _add(data1, r, -x)

def _get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s
def query(l, r):
    return _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)


ans = []
for q in range(Q):
    t, *cmd = map(int, readline().split())
    if t:
        s, t = cmd
        ans.append(str(query(s, t+1)))
    else:
        s, t, x = cmd
        add(s, t+1, x)
write("\n".join(ans))
write("\n")

