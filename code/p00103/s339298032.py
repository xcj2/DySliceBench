# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0103&lang=jp
"""
import sys



class Baseball():
    def __init__(self):
        self.score = 0
        self.out_count = 0
        self.base = [0, 0, 0]

    def event(self, e):
        if e == 'HIT':
            self.base.insert(0, 1)
            home = self.base.pop()
            if home:
                self.score += 1
        elif e == 'HOMERUN':
            self.score += self.base.count(1)
            self.score += 1
            self.base = [0, 0, 0]
        elif e == 'OUT':
            self.out_count += 1


def main(args):
    num = int(input().strip())
    for _ in range(num):
        b = Baseball()
        while b.out_count < 3:
            b.event(input().strip())
        print(b.score)


if __name__ == '__main__':
    main(sys.argv[1:])