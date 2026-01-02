
# A以下の数がN個与えられる。全て素因数分解せよ。
class SpeedPrime:
    # a以下の各数の最小の素因数を記録
    def __init__(self, a):
        self.d = [i for i in range(a+1)]

        i=2
        while i*i<=a:
            if self.d[i]==i:
                j=i*i
                while j<=a:
                    if self.d[j]==j:
                        self.d[j]=i
                    j+=i
            i+=1

    # nを高速素因数分解
    def fac(self, n):
        ret = dict()
        while n!=1:
            prime=self.d[n]
            if prime in ret:
                ret[prime]+=1
            else:
                ret[prime]=1
            n=n//prime
        return ret

import math
from functools import reduce
def gcd(numbers):
    return reduce(math.gcd, numbers)

n=int(input())
a=list(map(int,input().split()))

sp=SpeedPrime(max(a))

d=set()
pc=True
for i in a:
    prime=sp.fac(i)
    for k in prime.keys():
        if k in d:
            pc=False
            break
        else:
            d.add(k)

if pc:
    print("pairwise coprime")
    exit()

g=gcd(a)
if g==1:
    print("setwise coprime")
else:
    print("not coprime")
