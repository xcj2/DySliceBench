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

n, a, b, c, d = li()
a -= 1
b -= 1
s = ns()

no2_ac = not "##" in s[a:c]
no2_bd = not "##" in s[b:d]
yes3_bd = "..." in s[b-1:d+1]

if c < d:
    print("Yes" if no2_ac and no2_bd else "No")

else:
    print("Yes" if no2_ac and no2_bd and yes3_bd else "No")