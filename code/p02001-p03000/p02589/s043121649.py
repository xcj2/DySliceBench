import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class RollingHash(object):
    _base1, _base2 = 1007, 1009
    _mod1, _mod2 = 10**9 + 9, 10**9 + 7

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
    n = int(input())
    X = [input() for _ in range(n)]
    X.sort(key = len, reverse = 1)

    count = defaultdict(lambda:[0] * 26)
    ans = 0

    for S in X:
        k = len(S)
        rh = RollingHash(S)
        ok = [False] * 26
        ans += count[rh[1 : k]][ord(S[0]) - ord('a')]
        for i, c in enumerate(S):
            ok[ord(c) - ord('a')] = True
            for j in range(26):
                if ok[j]:
                    count[rh[i + 1 : k]][j] += 1
    print(ans)
resolve()