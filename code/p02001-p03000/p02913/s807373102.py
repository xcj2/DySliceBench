import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class RollingHash(object):
    _base1, _base2 = 1007, 1009
    _mod1, _mod2 = 10 ** 9 + 9, 10 ** 9 + 7

    def __init__(self,s):
        self._n=len(s)
        H1, H2 = [0] * (self._n + 1), [0] * (self._n + 1)
        P1, P2 = [1] * (self._n + 1), [1] * (self._n + 1)
        for i in range(self._n):
            H1[i + 1] = (H1[i] * self._base1 + ord(s[i])) % self._mod1
            H2[i + 1] = (H2[i] * self._base2 + ord(s[i])) % self._mod2
            P1[i + 1] = P1[i] * self._base1 % self._mod1
            P2[i + 1] = P2[i] * self._base2 % self._mod2
        self._H1, self._H2 = H1, H2
        self._P1, self._P2 = P1, P2

    def __len__(self):
        return self._n

    def __getitem__(self,x):
        l, r = x.start, x.stop;
        return ((self._H1[r] - self._P1[r - l] * self._H1[l] % self._mod1) % self._mod1,
                (self._H2[r] - self._P2[r - l] * self._H2[l] % self._mod2) % self._mod2)

from collections import defaultdict
def resolve():
    n=int(input())
    S=input()
    rh=RollingHash(S)

    def check(k):
        D=defaultdict(lambda:-1)
        for i in range(n-k+1):
            h=rh[i:i+k]
            if(D[h]!=-1):
                if(i-D[h]>=k): return True
            else:
                D[h]=i
        return False

    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    print(left)
resolve()