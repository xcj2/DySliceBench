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
    #return rnar()
    return (rr(), rr())

def solve(s, t):
    dp = ms(len(s)+1, len(t)+1)
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    tl = dp[len(s)][len(t)]
    #ppm(dp, len(s)+1, len(t)+1)

    if tl == 0: return ''
    
    i = len(s); j = len(t)
    ts = []
    while (i > 0) and (j > 0):
        if s[i-1] == t[j-1]:
            ts.append(s[i-1])
            i -= 1; j -= 1;
        else:
            if dp[i-1][j] == dp[i][j]:
                i -= 1
            else:
                j -= 1

    ts = "".join(reversed(ts))

    return ts

if __name__ == "__main__":
    #test_count = rri()
    test_count = 1
    for _ in range(test_count):
        input_data = read()
        result = solve(*input_data)
        print(result)
