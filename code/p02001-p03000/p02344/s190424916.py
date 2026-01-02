# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys
sys.setrecursionlimit(1000000)
N,Q = map(int,sys.stdin.readline().split())
qs = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param

parents = list(range(N))
diffs = [0]*N

def root(x):
    if parents[x]==x:
        return x
    else:
        pr = root(parents[x])
        diffs[x] += diffs[parents[x]]
        parents[x] = pr
        return pr

def weight(x):
    root(x)
    return diffs[x]

def diff(x,y):
    return weight(y)-weight(x)

def issame(x,y):
    return root(x) == root(y)

# make sure weight(y)-weight(x)=w
def merge(x,y,w):
    # assume ry > rx
    rx = root(x)
    ry = root(y)
    # incase rx!=x and ry !=y
    diff = weight(x)+(w-weight(y))
    if rx == ry:
        return False
    if rx < ry:
        rx,ry,diff = ry,rx,-diff
    diffs[ry] = diff
    parents[ry] = rx
    return True

for q in qs:
    if q[0]==0:
        x,y,z = q[1:]
        merge(x,y,z)
    else:
        x,y = q[1:]
        if root(x)==root(y):
            print(diff(x,y))
        else:
            print("?")
