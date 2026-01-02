#%%
import sys
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict
def primefactor(n):
     ans=defaultdict(int)
     for i in range(2,int(n**0.5+1)):
         while n%i==0:
             ans[i] += 1
             n //= i
     if n>1:
         ans[n]=1
     return dict(ans)

from itertools import product
from functools import reduce

def main():
    N=int(input())
    d=primefactor(N)

    ans = N - 1
    for v in product(*[range(i+1) for i in d.values()]):
        a = reduce(lambda x, y: x*y, [x**y for x, y in zip(d.keys(), v)])
        b = N // a
        ans = min(a-1 + b-1, ans)

    print(ans)

# %%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("abc144","c",main)


