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


def scan_domino(a: list, b: list):
    n = len(a)
    cnt = 0
    domino = ""

    while cnt < n:
        if a[cnt] == b[cnt]:
            domino += "x"
            cnt += 1
        else:
            domino += "y"
            cnt += 2

    return domino


def cnt_pattern(domino, mod):
    ans = 3 if domino[0] == "x" else 6
    for dleft, dright in zip(domino[:-1], domino[1:]):
        if dleft == "x" and dright == "x":
            ans *= 2
        elif dleft == "x" and dright == "y":
            ans *= 2
        elif dleft == "y" and dright == "x":
            ans *= 1
        else:
            ans *= 3

        ans %= mod

    return ans


n = ni()
a = lc()
b = lc()

MOD = 10**9 + 7

domino = scan_domino(a, b)
pats = cnt_pattern(domino, MOD)

print(pats)