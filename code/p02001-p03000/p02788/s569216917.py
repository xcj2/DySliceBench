import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
N,d,a = map(int,readline().split())

data0 = [0]*(N+1)
data1 = [0]*(N+1)
# 区間[l, r)に x を加算
def _add(data, k, x):
    while k <= N:
        data[k] += x
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1))
    _add(data0, r, x*(r-1))
    _add(data1, l, x)
    _add(data1, r, -x)

# 区間[l, r)の和を求める
def get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s
def query(l, r):
  return get(data1,r-1)*(r-1)+get(data0,r-1)-get(data1,l-1)*(l-1)-get(data0,l-1)

xh = []
for _ in range(N):
    x,h = map(int,readline().split())
    xh.append((x,h))

xh = sorted(xh)
xl = [x for x,h in xh]

for i in range(N):
    add(i+1, i+2, xh[i][1])

import bisect,math

ans = 0
for i in range(N):
    hp = query(i + 1, i + 2)
    #print(data0,data1,hp)    
    if hp > 0:
        count = math.ceil(hp/a)
        ans += count
        damage = count * a
        idx = bisect.bisect_right(xl, xl[i] + 2*d)
        add(i+1, idx+1, -damage)
print(ans)