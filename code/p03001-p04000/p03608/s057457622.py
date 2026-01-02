import heapq
N, M, R = map(int, input().split())

class Route:
    def __init__(self, B, C):
        self.next = points[B]
        self.distance = C
class Point:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.clear()
    def clear(self):
        self.distances = [-1] * 2
    def set(self, cur):
        self.distances[cur.srcid] = cur.distance
        return self.isWent(0) and self.isWent(1)
    def isWent(self, n):
        return self.distances[n] >= 0
    def addNeighbor(self, B, C):
        self.neighbors.append(Route(B, C))
    def optimize(self):
        self.neighbors = sorted(self.neighbors, key=lambda obj:obj.distance)

class MeetInfo:
    def __init__(self):
        self.clear()
    def clear(self):
        self.distance = -1
    def isMet(self):
        return self.distance >= 0

class Cursor:
    def __init__(self, ri, pt, meetinfo, dist=0):
        self.srcid = ri
        self.point = pt
        self.cur_route = 0
        self.distance = dist
        self.meetinfo = meetinfo
        if self.point.set(self):
            meetinfo.distance = self.point.distances[0] + self.point.distances[1]

    def cost(self):
        while self.cur_route < len(self.point.neighbors):
            rt = self.point.neighbors[self.cur_route]
            if not rt.next.isWent(self.srcid):
                break
            self.cur_route+= 1
        else:
            return None

        return self.distance + rt.distance

    def progress(self):
        nextrt = self.point.neighbors[self.cur_route]
        addcursor(Cursor(self.srcid, nextrt.next, self.meetinfo, self.distance + nextrt.distance))
        self.cur_route += 1
        addcursor(self)
    def __lt__(self, other):
        return True
points = [Point(i) for i in range(N+1)]

in_r = [ri for ri in map(int, input().split())]
for A, B, C in (map(int, input().split()) for _ in range(M)):
    points[A].addNeighbor(B, C)
    points[B].addNeighbor(A, C)

for x in points:
    x.optimize()

def addcursor(cur):
    c = cur.cost()
    if not c is None:
        heapq.heappush(hq, (c, cur))

def getRs(rs = None, cnt = -1, ret = None):
    if rs is None:
        rs = [False] * R
        ret = []
        cnt = R

    if cnt <= 0:
        yield ret
        return

    cnt -= 1

    for i in range(R):
        if not rs[i]:
            rs[i] = True
            ret.append(i)
            yield from getRs(rs, cnt, ret)
            ret.pop()
            rs[i] = False

Rmatrix = [[-1 for _ in range(R)] for _ in range(R) ]

for i in range(R):
    for j in range(R):
        if i >= j:
            continue

        meetinfo = MeetInfo()
        for x in points:
            x.clear()
        rs = [Cursor(i, points[ri], meetinfo)  for i, ri in enumerate((in_r[i], in_r[j]))]
        hq = []
        addcursor(rs[0])

        while not meetinfo.isMet():
            cost, cursor = heapq.heappop(hq)
            cursor.progress()

        Rmatrix[i][j] = meetinfo.distance
        Rmatrix[j][i] = meetinfo.distance

M = 10 ** 9
for r in getRs():
    #print(r)
    w = 0
    for i in range(R-1):
        w += Rmatrix[r[i]][r[i+1]]    
    M = min(M, w)

print(M)
