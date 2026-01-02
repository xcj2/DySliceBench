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

n,a,b,c,d = li_()
n += 1
s = ns()


if c < d:
    if "##" in s[a:c+1] or "##" in s[b:d+1]:
        print("No")

    else:
        print("Yes")

else:
    if (not "..." in s[b-1:d+2]):
        print("No")

    elif "##" in s[a:c + 1] or "##" in s[b:d + 1]:
        print("No")

    else:
        print("Yes")

