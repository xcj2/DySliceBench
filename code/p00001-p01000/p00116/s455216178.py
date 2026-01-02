# -*- coding: utf-8 -*-
"""
Rectangular Searching
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0116

"""
import sys


def solve(m, height, width):
    def calc_hist(m):
        hist = [[0]* width for _ in range(height)]
        for y, row in enumerate(m):
            for x, ch in enumerate(row):
                if ch == '.':
                    hist[y][x] = hist[y-1][x]+1 if y >0 else 1
        return hist

    def calc_area(hist):
        stack = []
        area = 0
        for x, h in enumerate(hist):
            if not stack or stack[-1][0] < h:
                stack.append((h, x))
            elif stack[-1][0] > h:
                while stack and stack[-1][0] >= h:
                    hh, left = stack.pop()
                    area = max(area, hh*(x-left))
                stack.append((h, left))
        return area

    hist = calc_hist(m)
    ans = 0
    for y in range(height):
        ans = max(ans, calc_area(hist[y]+[0])) #  [0]はヒストグラムを最後にリフレッシュして処理するために必要
    return ans


def main(args):
    while True:
        height, width = map(int, input().split())
        if height == 0 or width == 0:
            break
        m = [input() for _ in range(height)]
        ans = solve(m, height, width)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])

