import sys
# input関係の定義
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

# BEGIN CUT HERE
class RollingHash():
    """ロリハ。容易に衝突するので注意。"""
    BASE1 = 1007
    BASE2 = 2009
    MOD1 = 1000000007
    MOD2 = 1000000009

    def __init__(self, s, opt=2):
        self.n = len(s)
        self.opt = opt
        self.hash1 = [0] * (self.n + 1)
        self.power1 = [1] * (self.n + 1)
        if opt == 2:  # rollinghash by 2 mod
            self.hash2 = [0] * (self.n + 1)
            self.power2 = [1] * (self.n + 1)

        for i, e in enumerate(s):
            self.hash1[i + 1] = (self.hash1[i] * self.__class__.BASE1 + ord(e)) % self.__class__.MOD1
            self.power1[i + 1] = (self.power1[i] * self.__class__.BASE1) % self.__class__.MOD1
        if opt == 2:  # rollinghash by 2 mod
            for i, e in enumerate(s):
                self.hash2[i + 1] = (self.hash2[i] * self.__class__.BASE2 + ord(e)) % self.__class__.MOD2
                self.power2[i + 1] = (self.power2[i] * self.__class__.BASE2) % self.__class__.MOD2

    def get(self, l: int, r: int):
        res1 = self.hash1[r] - self.hash1[l] * self.power1[r - l] % self.__class__.MOD1
        if(res1 < 0):
            res1 += self.__class__.MOD1
        if self.opt == 2:
            res2 = self.hash2[r] - self.hash2[l] * self.power2[r - l] % self.__class__.MOD2
            if(res2 < 0):
                res2 += self.__class__.MOD2
        return (res1, res2) if self.opt == 2 else res1
# END CUT HERE

def ABC131E():
    N = ii()
    S = li()
    rh = RollingHash(S, opt=1)
    def check(n: int):
        d = dict()
        for i in range(N - n + 1):
            p = rh.get(i, i + n)
            if p in d:
                if(i - d[p] >= n):
                    return True
            else:
                d[p] = i
        return False
    ok, ng = 0, N // 2 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)



if __name__ == '__main__':
    ABC131E()
