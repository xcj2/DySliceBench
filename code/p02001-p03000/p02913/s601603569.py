import collections


class RollingHash:
    def __init__(self, s, base, mod):
        self.base = base
        self.mod = mod

        self.hash = [0]
        self.power = [1]
        for c in s:
            self.hash.append((self.hash[-1] * base + ord(c)) % mod)
            self.power.append(self.power[-1] * base % mod)

    def get(self, left, right):
        h = self.hash[right] - self.hash[left] * self.power[right - left]
        return (h + self.mod) % self.mod


n = int(input())
s = input().rstrip()
rh = RollingHash(s, base=26, mod=2**50 + 1)


def check(diff):
    d = collections.defaultdict(list)
    for i in range(n - diff + 1):
        h = rh.get(i, i + diff)
        d[h].append(i)
    for l in d.values():
        if max(l) - min(l) >= diff:
            return True
    return False


lo = 0
hi = n // 2 + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid
    else:
        hi = mid
print(lo)