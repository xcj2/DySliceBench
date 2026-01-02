# -*- coding: utf-8 -*-
"""
C - Grand Garden
https://atcoder.jp/contests/abc116/tasks/abc116_c

"""
import sys



def solve(heights):
    def w(arr):
        stack = []
        buff = []
        while arr:
            h = arr.pop(0)
            if h == 0:
                if buff:
                    stack.append(buff)
                    buff = []
            else:
                buff.append(h)
        if buff:
            stack.append(buff)
        return stack

    ans = 0
    stack = w(heights)
    while stack:
        arr = stack.pop()
        m = min(arr)
        ans += m
        s = w([a-m for a in arr])
        stack.extend(s)
    return ans


def main(args):
    N = int(input())
    heights = [int(h) for h in input().split()]
    ans = solve(heights)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
