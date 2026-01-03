import sys
readline = sys.stdin.readline
class UFP():
    def __init__(self, num):
        self.par = [-1]*num
        self.dist = [0]*num
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            res = 0
            xo = x
            while self.par[x] >= 0:
                res += self.dist[x]
                x = self.par[x]
            self.dist[xo] = res
            self.par[xo] = x
            return x
    
    def union(self, x, y, d):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
                x, y = y, x
                d = -d
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
            self.dist[ry] = d + self.dist[x] - self.dist[y]
            return True
        else:
            if d + self.dist[x] - self.dist[y]:
                return False
            return True           
    
INF = 3*10**9
def check():
    H, W = map(int, readline().split())
    N = int(readline())
    Hm = [INF]*H
    Wm = [INF]*W
    HP = [[] for _ in range(H)]
    WP = [[] for _ in range(W)]
    for _ in range(N):
        h, w, a = map(int, readline().split())
        h -= 1
        w -= 1
        Hm[h] = min(Hm[h], a)
        Wm[w] = min(Wm[w], a)
        HP[h].append((w, a))
        WP[w].append((h, a))
        
    Th = UFP(H)
    Tw = UFP(W)
    for h in range(H):
        L = len(HP[h]) 
        if L > 1:
            HP[h].sort()
            for i in range(L-1):
                wp, ap = HP[h][i]
                wn, an = HP[h][i+1]
                if not Tw.union(wp, wn, an-ap):
                    return False
    for w in range(W):
        L = len(WP[w]) 
        if L > 1:
            WP[w].sort()
            for i in range(L-1):
                hp, ap = WP[w][i]
                hn, an = WP[w][i+1]
                if not Th.union(hp, hn, an-ap):
                    return False
    
    cmh = [INF]*H
    for h in range(H):
        rh = Th.find(h)
        cmh[rh] = min(cmh[rh], Th.dist[h])
    cmw = [INF]*W
    for w in range(W):
        rw = Tw.find(w)
        cmw[rw] = min(cmw[rw], Tw.dist[w])
    
    for h in range(H):
        if Hm[h] - Th.dist[h] + cmh[Th.find(h)] < 0:
            return False
    for w in range(W):
        if Wm[w] - Tw.dist[w] + cmw[Tw.find(w)] < 0:
            return False
    return True

print('Yes' if check() else 'No')