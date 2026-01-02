from operator import itemgetter, attrgetter

class P:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, p): return P(self.x + p.x, self.y + p.y)
    def __sub__(self, p): return P(self.x - p.x, self.y - p.y)
    def dot(self, p): return (self.x*p.x + self.y*p.y)
    def cross(self, p): return (self.x*p.y - self.y*p.x)
    def abs(self): return (abs(self.x) + abs(self.y))

def convex_hull(Ps):
    Ps.sort(key=attrgetter('x', 'y'))
    ret1, ret2 = list(), list()
    for i in range(len(Ps)):
        k = len(ret1)
        while k>=2 and (Ps[i]-ret1[k-1]).cross(ret1[k-1]-ret1[k-2]) <= 0:
            ret1.pop()
            k = len(ret1)
        ret1.append(Ps[i])
    for i in range(len(Ps)):
        k = len(ret2)
        while k>=2 and (Ps[i]-ret2[k-1]).cross(ret2[k-1]-ret2[k-2]) >= 0:
            ret2.pop()
            k = len(ret2)
        ret2.append(Ps[i])
    return ret1 + ret2[::-1]

N = int(input())
Ps = list()
for i in range(N):
    x, y = list(map(int, input().split()))
    Ps.append(P(x, y))

# produce convex hull
CPs = convex_hull(Ps)

# brute force
ans = 0
for i in range(len(CPs)):
    for j in range(i, len(CPs)):
        mdis = (CPs[i]-CPs[j]).abs()
#        print(i, j, mdis)
        if ans < mdis: ans = mdis

print (ans)
