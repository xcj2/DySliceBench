from collections import defaultdict as dd

n, mm = [int(i) for i in input().split()]
c = 0
A = []

m = dd(tuple)

for i in range(n):
    B = input()
    for j in range(mm):
        m[(i, j)]=c
        c+=1
    A.append([i=='#' for i in B])

par = [i for i in range(c)]

def find(a):
    if par[a] == a:
        return a
    par[a] = find(par[a])
    return par[a]

def unite(a, b):
    if a < b:
        a, b = b, a
    par[find(a)] = find(b)

def issafe(x,y):
    return x>=0 and x<n and y>=0 and y<mm

for i in range(n):
    for j in range(mm):
        dx = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        for k in range(len(dx)):
            if issafe(i+dx[k][0], j+dx[k][1]) and A[i][j] != A[i+dx[k][0]][j+dx[k][1]]:
                unite(m[(i, j)], m[(i+dx[k][0], j+dx[k][1])])
                
bl = [0]*c
wh = [0]*c

for i in range(n):
    for j in range(mm):
        if A[i][j] == 1:
            bl[find(m[i, j])]+=1
        else:
            wh[find(m[i, j])]+=1

ans = 0
for i in range(c):
    ans += bl[i]*wh[i]

print(ans)
