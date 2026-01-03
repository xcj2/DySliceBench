import sys
input = lambda: sys.stdin.readline().rstrip()

def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x,y = y,x

    parents[x] += parents[y]
    parents[y] = x

def same(x,y):
    return find(x) == find(y)

N = int(input())

parents = [-1] * N
ver_x = []
ver_y = []
for i in range(N):
    x,y = map(int, input().split())
    ver_x.append((x,i))
    ver_y.append((y,i))

ver_x.sort()
ver_y.sort()

edge_list = []

for i in range(N-1):
    x_dist = ver_x[i+1][0]-ver_x[i][0]
    y_dist = ver_y[i+1][0]-ver_y[i][0]

    edge_list.append((x_dist, ver_x[i+1][1], ver_x[i][1]))
    edge_list.append((y_dist, ver_y[i+1][1], ver_y[i][1]))

ans = 0

edge_list.sort()

for w,s,t in edge_list:
    if not same(s,t):
        union(s,t)
        ans += w
print(ans)