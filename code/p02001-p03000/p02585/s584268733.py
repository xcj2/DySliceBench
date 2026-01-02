n,k = map(int,input().split())
p = list(map(int,input().split()))
for i in range(n):
    p[i]-=1
c = list(map(int,input().split()))
par = [-1 for i in range(n)]
deep = [1 for i in range(n)]
ma = max(c)
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
        if deep[x] > deep[y]:
            par[x] += par[y]
            par[y] = x
        elif deep[x] < deep[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            deep[x] += 1
        return True
def same(x,y):
    return find(x) == find(y)
def size(x):
    return -par[find(x)]
for i in range(n):
    unite(i,p[i])
for i in range(n):
    if par[i] >= 0:
        continue
    else:
        t = -par[i]
        if t >= k:
            for j in range(k):
                tmp = 0
                tmp2 = p[i]
                for l in range(j+1):
                    tmp += c[tmp2]
                    tmp2 = p[tmp2]
                tmp3 = p[i]
                ma = max(ma,tmp)
                for l in range(t):
                    tmp += c[tmp2]
                    tmp -= c[tmp3]
                    tmp2 = p[tmp2]
                    tmp3 = p[tmp3]
                    ma = max(ma,tmp)
        else:
            tmpp = p[i]
            tmp7 = 0
            for j in range(t):
                tmp7 += c[tmpp]
                tmpp = p[tmpp]
            if tmp7 <= 0:
                for j in range(t):
                    tmp = 0
                    tmp2 = p[i]
                    for l in range(j+1):
                        tmp += c[tmp2]
                        tmp2 = p[tmp2]
                    tmp3 = p[i]
                    ma = max(ma,tmp)
                    for l in range(t):
                        tmp += c[tmp2]
                        tmp -= c[tmp3]
                        tmp2 = p[tmp2]
                        tmp3 = p[tmp3]
                        ma = max(ma,tmp)
            else:
                g = k//t
                g2 = k//t - 1
                ma2 = 0
                ma3 = 0
                for j in range(k % t):
                    tmp = 0
                    tmp2 = p[i]
                    for l in range(j+1):
                        tmp += c[tmp2]
                        tmp2 = p[tmp2]
                    tmp3 = p[i]
                    ma2 = max(ma2,tmp)
                    for l in range(t):
                        tmp += c[tmp2]
                        tmp -= c[tmp3]
                        tmp2 = p[tmp2]
                        tmp3 = p[tmp3]
                        ma2 = max(ma2,tmp)
                ma2 += tmp7 * g
                for j in range(t):
                    tmp = 0
                    tmp2 = p[i]
                    for l in range(j+1):
                        tmp += c[tmp2]
                        tmp2 = p[tmp2]
                    tmp3 = p[i]
                    ma3 = max(ma3,tmp)
                    for l in range(t):
                        tmp += c[tmp2]
                        tmp -= c[tmp3]
                        tmp2 = p[tmp2]
                        tmp3 = p[tmp3]
                        ma3 = max(ma3,tmp)
                ma3 += tmp7 * g2
                ma = max(max(ma,ma2),ma3)
print(ma)