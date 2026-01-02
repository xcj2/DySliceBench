import sys
input = lambda: sys.stdin.readline().rstrip()

n,q = map(int, input().split())

parents = [-1] * n

def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x,y = y, x

    parents[x] += parents[y]
    parents[y] = x     

def same(x,y):
    return find(x) == find(y)

for i in range(q):
    com,x,y = map(int, input().split())

    if com == 0:
        union(x, y)
    else:
        if same(x, y):
            print(1)
        else:
            print(0)        

