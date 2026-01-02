def rr(): return input().rstrip()
def rri(): return int(rr())
def rrl(): return list(map(int, rr().split()))
def rrt(): return tuple(map(int, rr().split()))
from collections import defaultdict
def mus(d=lambda: 0): return defaultdict(lambda: defaultdict(d))
def dd0(d=lambda: 0): return defaultdict(d)
def ms(x, y, d=0): return [[0]*y for i in range(x)]
def ar(x, d=0): return [d]*x
def ppm(m, n=0, x=0, y=0): print("\n".join(("\t".join((str(m[j][i]) for j in range(y or n))) for i in range(x or n))))
def ppa(a, n): print("\t".join(map(str, a[0:n])))
def ppl(a=0, x=[1]): x[0]=a or (x[0]+1); print("-"+"- -"*14+"-# "+str(x[0]-2)+" #-"+"- -"*14+"-")
def fltn(a): (i for sub in a for i in sub)
def yn(x): return "YES" if x else "NO"
from itertools import accumulate
from itertools import groupby
def grp(x): return ((i, sum(1 for _ in g)) for i, g in groupby(x))
import math
#def rnar(): return (*rrl(), rrl())
#def rn(): return (*rrl(),)
def dpp(a, b=""): print(")#| {} |#(o) ? {} ? (".format(a, b))

def read():
    n, w = rrl()
    l = [rrt() for _ in range(n)]

    return n, w, l

def solve(n, w, l):
    dp = ms(w+1, n+1)

    for wi in range(1, w+1):
        for ii in range(1, n+1):
            if l[ii-1][0] > wi:
                dp[wi][ii] = dp[wi][ii-1]
            else:
                dp[wi][ii] = max(
                        dp[wi][ii-1],
                        dp[wi-l[ii-1][0]][ii-1] + l[ii-1][1],
                        )
    #ppm(dp, w+1, n+1)

    ans = dp[w][n]
    return ans

if __name__ == "__main__":
    #test_count = rri()
    test_count = 1
    for _ in range(test_count):
        input_data = read()
        result = solve(*input_data)
        print(result)
