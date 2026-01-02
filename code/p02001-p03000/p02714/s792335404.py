n = int(input())
s = str(input())
r = []
g = []
def right(r,g):
    return (max(r,g)+(abs(r-g)))
def left(r,g):
    return (min(r,g)-(abs(r-g)))
def half(r,g):
    return ((r+g)//2)
for i in range(n):
    if s[i] == "R":
        r.append(i)
    elif s[i] == "G":
        g.append(i)
ans = len(r)*len(g)*(n-(len(r)+len(g)))
for i in range(len(r)):
    for j in range(len(g)):
        t = left(r[i],g[j])
        f = right(r[i],g[j])
        h = half(r[i],g[j])
        if f < n:
            if s[f] == "B":
                ans -= 1
        if 0 <= t:
            if s[t] == "B":
                ans -= 1
        if abs(r[i]-g[j])%2 == 0:
            if s[h] == "B":
                ans -= 1
print(ans)