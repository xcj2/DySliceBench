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


class RollingHash(object):
    def __init__(self, source: str, base=10**9+7, mod=(1<<64)-1):
        self.source = source
        self.base = base
        self.mod = mod
        self.hash_from_zero_to = self._get_hash_from_zero_to()
        self.base_pow = self._get_base_pow()

    # 文字列sourceの区間 [0, right) のハッシュ値を前計算する
    def _get_hash_from_zero_to(self):
        hash_from_zero_to = [0]
        for si in self.source:
            hash_from_zero_to.append((hash_from_zero_to[-1] * self.base + ord(si)) % self.mod)

        return hash_from_zero_to

    # base値をi回掛けてmodをとった値を前計算する
    def _get_base_pow(self):
        base_pow = [1]
        for i in range(len(self.source)):
            base_pow.append(base_pow[-1] * self.base % self.mod)

        return base_pow

    # 文字列sourceの区間 [left, right) のハッシュを取得する
    def get_hash(self, left: int, right: int):
        return (self.hash_from_zero_to[right]
                - self.hash_from_zero_to[left] * self.base_pow[right - left]) % self.mod


def binsearch(func, rh: RollingHash, ok: int, ng: int):
    source_length = len(rh.source)
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if func(rh, mid, source_length):
            ok = mid
        else:
            ng = mid

    return ok


# 題意を満たす長さtarget_lengthの文字列があるか判定
def judge(rh: RollingHash, target_length: int, source_length: int):
    memo = {}
    for start_idx in range(source_length - target_length + 1):
        cur_hash = rh.get_hash(start_idx, start_idx + target_length)
        if cur_hash in memo:
            if start_idx - memo[cur_hash] >= target_length:
                return True
        else:
            memo[cur_hash] = start_idx

    return False


n = ni()
s = ns()

rh = RollingHash(s)
print(binsearch(judge, rh, 0, n//2 + 2))