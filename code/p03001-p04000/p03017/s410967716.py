#!/usr/bin/env python
# coding: utf-8

def readInt():
    return int(input())

def readList():
    return list(input().split())

def readListI():
    return list(map(int, input().split()))

def check(s, x_from, x_to):
    for x in range(x_from, x_to):
        can_jump = False
        for dx in range(0, 2):
            if s[x+dx] == '.':
                can_jump = True
                break
        if not can_jump:
            return False
    return True


def main():
    n, a, b, c, d = readListI()
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    s = input()

    if c > d:
        # 抜く必要があり、...がb-1<=x<=dにないといけないのでその判定をする
        can_swap = False
        for x in range(b-1, d):
            can_swap_here = True
            for dx in range(0, 3):
                if s[x+dx] == '#':
                    can_swap_here = False
                    break
            if can_swap_here:
                can_swap = True
                break
        if not can_swap:
            print("No")
            return

    # それぞれがたどりつけるか (##がないか) を調べれば良い
    if not check(s, a, c):
        print("No")
        return
    if not check(s, b, d):
        print("No")
        return
    print("Yes")


if __name__ == '__main__':
    main()
