# Input
import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


def aok_turn(aoki: str, tolow: str, toup: str, lower: int, upper: int, amin: int, amax: int):
    if aoki == tolow:
        upper = min(amax, upper + 1)
    elif aoki == toup:
        lower = max(amin, lower - 1)

    return lower, upper


def tak_turn(taki: str, tolow: str, toup: str, lower: int, upper: int, amin:int, amax: int):
    if taki == tolow:
        lower = min(amax, lower + 1)
    elif taki == toup:
        upper = max(amin, upper - 1)

    return lower, upper


def on_board(lower: int, upper: int, amin: int, amax: int):
    if lower < upper and upper > amin and lower < amax:
        return True
    else:
        return False


def judge(tak: str, aok: str, tolow: str, toup: str, start: int, amin: int, amax: int) -> bool:
    lower = amin
    upper = amax
    for aoki, taki in zip(aok, tak):
        lower, upper = aok_turn(aoki, tolow, toup, lower, upper, amin, amax)
        lower, upper = tak_turn(taki, tolow, toup, lower ,upper, amin, amax)
        if not on_board(lower, upper, amin, amax):
            return False

    return True if lower <= start < upper else False


h,w,n = li()
sr, sc = li_()
tak = ns()[::-1]
aok = ns()[::-1]

L = 'L'
R = 'R'
U = 'U'
D = 'D'

lr = judge(tak, aok, L, R, sc, 0, w)
ud = judge(tak, aok, U, D, sr, 0, h)

print("YES") if lr and ud else print("NO")