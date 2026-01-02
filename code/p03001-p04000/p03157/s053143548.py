from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.v = [-1] * n

    def find(self, x):
        if self.v[x] < 0:
            return x
        else:
            self.v[x] = self.find(self.v[x])
            return self.v[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.v[x] > self.v[y]:
                x, y = y, x
            self.v[x] += self.v[y]
            self.v[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.v[self.find(x)]


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]

    d = (1, 0), (-1, 0), (0, 1), (0, -1)

    uf = UnionFind(h * w * 2)
    for r in range(h):
        for c in range(w):
            id_ = (r * w + c) + (h * w if s[r][c] == '#' else 0)
            for dr, dc in d:
                nr = r + dr
                if nr < 0 or h <= nr:
                    continue
                nc = c + dc
                if nc < 0 or w <= nc:
                    continue
                if s[nr][nc] == s[r][c]:
                    continue
                nid = (nr * w + nc) + (h * w if s[nr][nc] == '#' else 0)
                uf.unite(id_, nid)

    for r in range(h):
        for c in range(w):
            id_ = (r * w + c) + (h * w if s[r][c] == '#' else 0)
            uf.find(id_)
            # 葉の親が更新されていなかったために、連結成分の大きさが小さく判定されていた

    checked = [False] * (h * w * 2)
    ctr_dot = Counter(uf.v[:h * w])
    ctr_sharp = Counter(uf.v[h * w:])

    ret = 0
    for r in range(h):
        for c in range(w):
            id_ = (r * w + c) + (h * w if s[r][c] == '#' else 0)
            root = uf.find(id_)

            if checked[root]:
                continue

            checked[root] = True

            dot = ctr_dot[root]
            sharp = ctr_sharp[root]

            if root < h * w:
                dot += 1
            else:
                sharp += 1

            ret += dot * sharp

    print(ret)


if __name__ == '__main__':
    main()
