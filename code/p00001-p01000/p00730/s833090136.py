# https://onlinejudge.u-aizu.ac.jp/problems/1149


class Cake:
    def __init__(self, w, d):
        self.w = w
        self.d = d

    def area(self):
        return self.w * self.d

    def cut(self, s):
        perimeter = self.w * 2 + self.d * 2
        s %= perimeter
        if s < self.w:
            return [Cake(s, self.d), Cake(self.w - s, self.d)]
        elif s < self.w + self.d:
            l = s - self.w
            return [Cake(self.w, l), Cake(self.w, self.d - l)]
        elif s < self.w + self.d + self.w:
            l = s - (self.w + self.d)
            return [Cake(self.w - l, self.d), Cake(l, self.d)]
        else:
            l = s - (self.w + self.d + self.w)
            return [Cake(self.w, self.d - l), Cake(self.w, l)]

    def __repr__(self):
        return '(w {}, d {})'.format(self.w, self.d)


def solve(Q, n, w, d):
    cakes = [Cake(w, d)]
    for p, s in Q:
        # print(cakes)
        cut_cake = cakes.pop(p)
        cake1, cake2 = cut_cake.cut(s)
        if cake1.area() > cake2.area():
            cake2, cake1 = cake1, cake2
        cakes.append(cake1)
        cakes.append(cake2)

    # print(cakes)
    cakes.sort(key=lambda cake: cake.area())
    areas_str = []
    for cake in cakes:
        area_str = str(cake.area())
        areas_str.append(area_str)
    print(' '.join(areas_str))


if __name__ == "__main__":
    while True:
        n, w, d = list(map(int, input().split()))
        if n == 0 and w == 0 and d == 0:
            break
        Q = []
        for _ in range(n):
            p, s = list(map(int, input().split()))
            Q.append((p-1, s))
        solve(Q, n, w, d)

