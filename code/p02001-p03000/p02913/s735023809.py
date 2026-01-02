# ABC141E - Who Says a Pun?
class RollingHash:
    def __init__(self, source: str, base=1000000007, mod=9007199254740997):
        self.source = source
        self.length = len(source)
        self.base = base
        self.mod = mod
        self.hash = self._get_hash_from_zero()
        self.power = self._get_base_pow()

    def _get_hash_from_zero(self):  # compute hash of interval [0, right)
        cur, hash_from_zero = 0, [0]
        for e in self.source:
            cur = (cur * self.base + ord(e)) % self.mod
            hash_from_zero.append(cur)
        return hash_from_zero

    def _get_base_pow(self):  # computer mod of power of base
        cur, power = 1, [1]
        for i in range(self.length):
            cur *= self.base % self.mod
            power.append(cur)
        return power

    def get_hash(self, l: int, r: int):  # compute hash of interval [left, right)
        return (self.hash[r] - self.hash[l] * self.power[r - l]) % self.mod


def main():
    N = int(input())
    S = input().rstrip()
    rh, ok, ng = RollingHash(S), 0, N // 2 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        flg, memo = 0, set()
        for i in range(N - 2 * mid + 1):
            memo.add(rh.get_hash(i, i + mid))
            if rh.get_hash(i + mid, i + 2 * mid) in memo:
                flg = 1
                break
        if flg:
            ok = mid  # next mid will be longer
        else:
            ng = mid  # next mid will be shorter
    print(ok)  # max length of substrings appeared twice or more


if __name__ == "__main__":
    main()