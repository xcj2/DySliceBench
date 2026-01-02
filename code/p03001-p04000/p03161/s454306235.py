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
    a, b = rrl();
    return (a, b, rrl())
    return (0,)

def solve(n, k, arr):
    if k > len(arr):
        k = len(arr)
    dp = ar(n)
    dp[0] = 0
    for i in range(1, k):
        dp[i] = min(dp[j] + abs(arr[i]-arr[j]) for j in range(0, i))
        #dpp("HAr2", "HA")

    for i in range(k, n):
        #dpp("HA", i)
        dp[i] = min(dp[j] + abs(arr[i]-arr[j]) for j in range(i-k, i))

    #dpp(dp)
    ans = dp[-1]

    return ans

if __name__ == "__main__":
    #test_count = rri()
    test_count = 1
    for _ in range(test_count):
        input_data = read()
        result = solve(*input_data)
        print(result)
