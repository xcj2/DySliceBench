# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0104&lang=jp
"""
import sys


class MagicalTiles():
    def __init__(self, data):
        self.map = data[:]
        self.pos = (0, 0)
        self.path = [(0, 0)]
        self.mark = self.map[0][0]
        self.loop = False

    def move(self):
        x, y = self.pos[0], self.pos[1]
        self.mark = self.map[y][x]
        if self.mark == '>':
            x += 1
        elif self.mark == '<':
            x -= 1
        elif self.mark == '^':
            y -= 1
        elif self.mark == 'v':
            y += 1
        if self.mark != '.' and (x, y) in self.path:
            self.loop = True
        else:
            self.path.append((x, y))
        self.pos = (x, y)


def main(args):
    # data = []
    # data.append('>>>v..>>>v')
    # data.append('...v..^..v')
    # data.append('>>>>>>^..v')
    # data.append('.........v')
    # data.append('.v<<<<...v')
    # data.append('.v.v.^...v')
    # data.append('.v.v.^<<<<')
    # data.append('.v.v.....v')
    # data.append('.v...^...v')
    # data.append('.>>>>^....')
    #
    # data = []
    # data.append('>>>>>>>>>v')
    # data.append('.........v')
    # data.append('.........v')
    # data.append('>>>>v....v')
    # data.append('^...v....v')
    # data.append('^<<<<<<<<<')
    while True:
        h, w = [int(x) for x in input().split(' ')]
        if h == 0 and w == 0:
            break
        data = [input() for _ in range(h)]

        m = MagicalTiles(data)
        while m.mark != '.':
            m.move()
            if m.loop:
                break
        if m.loop:
            print('LOOP')
        else:
            print(m.pos[0], m.pos[1])


if __name__ == '__main__':
    main(sys.argv[1:])