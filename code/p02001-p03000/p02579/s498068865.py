import sys

class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

def solve():
    readline = sys.stdin.readline
    H, W = map(int, readline().split())
    ch, cw = map(int, readline().split())
    dh, dw = map(int, readline().split())
    S = ['#'] * (W+2)
    for _ in range(H):
        S += ['#'] + list(readline().rstrip()) + ['#']
    S += ['#'] * (W+2)
    H += 2
    W += 2

    uf = UnionFind(H*W)
    for i in range(H*W):
        if S[i] == '#':
            continue
        for d in [-W, -1, 1, W]:
            if S[i+d] == '.':
                uf.union(i, i+d)

    now = ch*(W) + cw
    goal = dh*(W) + dw
    # print(now, goal)
    # print(uf.find(now), uf.find(goal))
    if uf.same(now, goal):
        print(0)
        return
    ans = 0
    q = set()
    q.add(now) 
    next_area = set() 
    visited = [False] * (H*W)

    # for i in range(H):
    #     print(S[6*i:6*i+6])
    while True:
        while q:
            x = q.pop()
            if x == goal:
                print(ans)
                return
            visited[x] = True
            for dy in [-2*W, -W, 0, W, 2*W]:
                for dx in [-2, -1, 0, 1, 2]:
                    xx = x + dy + dx
                    if 0 <= xx < W*H and S[xx] == '.' and not visited[xx]:
                        if uf.same(x, xx):
                            q.add(xx)
                        else:
                            next_area.add(xx)
        if next_area:
            q = next_area
            next_area = set()
        else:
            print(-1)
            return 
        ans += 1

if __name__ == '__main__':
    solve()
