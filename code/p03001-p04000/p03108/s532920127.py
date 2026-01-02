import sys
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
X = []
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    X.append((a, b))

X.reverse()

def Find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = Find(par[x], par)
        return par[x]

def Unite(x, y, par, rank):
    x = Find(x, par)
    y = Find(y, par)

    if x != y:
        if rank[x] < rank[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def Same(x, y, par):
    return Find(x, par) == Find(y, par)

def Size(x, par):
    return -par[Find(x, par)]

temp = n*(n-1)//2
ans = [0]*m

par = [-1]* n
rank = [0]*n

for i in range(m):
    a, b = X[i]
    ans[i] = temp
    if Same(a, b, par):
        continue
    else:
        pre_a = Size(a, par)
        pre_b = Size(b, par)
        Unite(a, b, par, rank)
        temp -= pre_a*pre_b
        #if temp <= 0:
        #temp = 0

ans.reverse()
#print(ans)
for i in range(len(ans)):
    print(ans[i])