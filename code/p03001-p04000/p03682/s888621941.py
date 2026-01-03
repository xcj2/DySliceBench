def find(u,x):
    if u[x]<0:
        return x
    u[x] = find(u,u[x])
    return u[x]

def unite(u,a,b):
    a = find(u,a)
    b = find(u,b)
    if a == b:
        return False
    if u[b] < u[a]:
        a,b = b,a
    u[a] += u[b]
    u[b] = a
    return True

def same(u,x,y):
    return find(u,x) == find(u,y)

n = int(input())
l = list()
for i in range(n):
  x,y = map(int,input().split())
  l.append((x,y,i))
l.sort()
uf = [-1]*(n+1)
ed = list()
for i in range(n-1):
  ed.append((l[i][2],l[i+1][2],l[i+1][0]-l[i][0]))
l.sort(key=lambda x:x[1])
for i in range(n-1):
  ed.append((l[i][2],l[i+1][2],l[i+1][1]-l[i][1]))
ed.sort(key=lambda x:x[2])
ans = 0
for x,y,d in ed:
  if not same(uf,x,y):
    unite(uf,x,y)
    ans += d
print(ans)