# -*- coding: utf-8 -*-

n, a, b, c, d = map(int, input().split())
s = input()


def two_rocks(li):
    if "##" in li:
        return True
    else:
        return False


def three_spaces(li):
    if "..." in li:
        return True
    else:
        return False


def solve():
    if two_rocks(s[a-1:c-1]):
        return False
    if two_rocks(s[b-1:d-1]):
        return False
    if d < c:
        if three_spaces(s[b-2:d+1]):
            return True
        else:
            return False
    else:
        return True


ans = "Yes" if solve() else "No"
print(ans)
