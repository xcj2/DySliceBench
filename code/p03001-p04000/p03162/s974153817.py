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
    n = rri()
    l = [rrt() for _ in range(n)]

    return n, l
    return (0,)

def solve(n, l):
    dp0 = ar(n)
    dp1 = ar(n)
    dp2 = ar(n)
    #dpp(l)

    dp0[0] = l[0][0]
    dp1[0] = l[0][1]
    dp2[0] = l[0][2]

    for i in range(1, n):
        dp0[i] = max(dp1[i-1], dp2[i-1]) + l[i][0]
        dp1[i] = max(dp0[i-1], dp2[i-1]) + l[i][1]
        dp2[i] = max(dp1[i-1], dp0[i-1]) + l[i][2]

    #dpp(dp0)
    #dpp(dp1)
    #dpp(dp2)

    ans = max(dp0[-1], dp1[-1], dp2[-1])
    return ans

if __name__ == "__main__":
    #test_count = rri()
    test_count = 1
    for _ in range(test_count):
        input_data = read()
        result = solve(*input_data)
        print(result)
