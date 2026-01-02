# -*- coding: utf-8 -*-
"""
Pattern - Largest Rectangle
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_B&lang=jp

"""
import sys


def solve(H, W, grid):
    def calc_hist(m):
        ans = [[0] * W for _ in range(H)]
        for y, row in enumerate(m):
            for x, ch in enumerate(row):
                if ch == '0':
                    ans[y][x] = ans[y - 1][x] + 1 if y > 0 else 1
        return ans

    def calc_area(hist):
        stack = []
        area, left = 0, 0
        for x, h in enumerate(hist):
            if not stack or stack[-1][0] < h:
                stack.append((h, x))
            elif stack[-1][0] > h:
                while stack and stack[-1][0] >= h:
                    hh, left = stack.pop()
                    area = max(area, hh*(x-left))
                stack.append((h, left))
        return area

    hist = calc_hist(grid)
    ans = 0
    for y in range(H):
        ans = max(ans, calc_area(hist[y]+[0]))
    return ans


def main(args):
    H, W = map(int, input().split())
    grid = [input().replace(' ', '') for _ in range(H)]
    ans = solve(H, W, grid)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])

