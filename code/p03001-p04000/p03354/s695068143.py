def LI(): return [int(i) for i in input().split()]
def LI_(): return [int(i)-1 for i in input().split()]
def LIR_(n): return [LI_() for i in range(n)]
def D():
    n, m = LI()
    p = LI_()
    xy = LIR_(m)
    size = [1 for _ in range(n)]
    height = [1 for _ in range(n)]
    par = [i for i in range(n)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        if s1 != s2:
            if height[s1] < height[s2]:
                par[s1] = s2
                size[s2] += size[s1]
                size[s1] = 0
            else:
                par[s2] = s1
                size[s1] += size[s2]
                size[s2] = 0
                if height[s1] == height[s2]:
                    height[s1] += 1
 
    for x,y in xy:
        union(x, y)
    ans = 0
    for i in range(n):
        if find(p[i]) == find(i):
            ans += 1
    
    print(ans)
D()
