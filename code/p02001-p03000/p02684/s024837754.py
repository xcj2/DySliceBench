import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()
A = LMI()

d = dict()
seen = set()
i = 0
cur = 0
while True:
    if i > 0:
        cur = A[cur] - 1
    if cur in seen:
        break
    d[i] = cur
    seen.add(cur)
    i += 1

def get_loop_size(start):
    c = start
    size = 0
    while size == 0 or c != start:
        c = A[c] - 1
        size += 1
    return size

for k, v in d.items():
    if v == cur:
        start = k
        break
loop_size = get_loop_size(d[start])
if K < start:
    print(d[K] + 1)
else:
    idx = start + (K - start) % loop_size
    print(d[idx] + 1)