import sys
stdin = sys.stdin

from itertools import accumulate

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


def yoko(h, w):
    return 0 if h%3 == 0 else w

def tate(h, w):
    return 0 if w%3 == 0 else h

def tee1(h, w):
    h1 = h//3
    w1 = w//2

    top = h1 * w
    lef = (h-h1)*w1
    rig = (h-h1)*(w-w1)

    return max(abs(top-lef), abs(top-rig), abs(lef-rig))

def tee2(h, w):
    h1 = h // 3 + 1
    w1 = w // 2

    top = h1 * w
    lef = (h - h1) * w1
    rig = (h - h1) * (w - w1)

    return max(abs(top - lef), abs(top - rig), abs(lef - rig))

def to1(h, w):
    w1 = w//3
    h1 = h//2

    lef = w1*h
    top = (w-w1)*h1
    bot = (w-w1)*(h-h1)

    return max(abs(lef-top), abs(lef-bot), abs(top-bot))


def to2(h, w):
    w1 = w // 3 + 1
    h1 = h // 2

    lef = w1 * h
    top = (w - w1) * h1
    bot = (w - w1) * (h - h1)

    return max(abs(lef - top), abs(lef - bot), abs(top - bot))


def judge(h, w):
    return min(yoko(h, w), tate(h, w), tee1(h, w), tee2(h, w), to1(h, w), to2(h, w))

h, w = li()

ans = judge(h, w)
print(ans)