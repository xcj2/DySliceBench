# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1149&lang=jpfrom bisect import bisect_left
# 対称性から s <= w + h の範囲のみを考えれば良い
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

class Cake:
    def __init__(self, h, w):
        self.height = h
        self.width = w
    
    def circumference(self):
        return 2 * (self.height + self.width)
    
    def area(self):
        return self.height * self.width


def main():
    ans = []

    while True:
        n,w,d = map(int, readline().split())
        if (n, w, d) == (0, 0, 0):
            break

        piece = [Cake(d, w)]
        for _ in range(n):
            p, s = map(int, readline().split())
            p -= 1
            
            c = piece.pop(p)
            s %= c.circumference() // 2
            if s < c.width:
                h1, h2 = c.height, c.height
                w1, w2 = min(s, c.width - s), max(s, c.width - s)
            else:
                h = s - c.width
                h1, h2 = min(h, c.height - h), max(h, c.height - h)
                w1, w2 = c.width, c.width
            
            """
            if h == c.height:
                h1, h2 = h, h
                w1, w2 = min(w, c.width - w), max(w, c.width - w)
            else:
                h1, h2 = min(h, c.height - h), max(h, c.height - h)
                w1, w2 = w, w
            """

            piece.append(Cake(h1, w1))
            piece.append(Cake(h2, w2))

        ans.append(sorted([p.area() for p in piece]))
    
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
