## x座標かy座標で隣り合わないものを繋ぐ辺は間に存在する点との接続で事足りるので不要
N = int(input())
city = []
for i in range(N):
    city_i = [i] + list(map(int,input().split()))
    city.append(city_i)
#print(city)

edges = []
city.sort(key = lambda x:x[1])
for i in range(N-1):
    w = city[i+1][1] - city[i][1]
    edges.append((w,city[i][0],city[i+1][0]))

city.sort(key = lambda x:x[2])
for i in range(N-1):
    w = city[i+1][2] - city[i][2]
    edges.append((w,city[i][0],city[i+1][0]))
edges.sort()
#print(edges)



def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

def same(x,y):
    return find(x) == find(y)

par = [-1]*N

ans = 0
for e in edges:
    if same(e[1],e[2]):
        continue
    unite(e[1],e[2])
    ans += e[0]
print(ans)

