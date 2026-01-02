def main():
    import sys
    input = sys.stdin.readline

    class RollingHash:
        def __init__(self, S, base, mod):
            self.S = S
            self.mod = mod
            self._hash = [0] * (len(S) + 1)
            self.pow = [1] * (len(S) + 1)

            for i, s in enumerate(S):
                self._hash[i + 1] = (self._hash[i] * base + s) % mod
                self.pow[i + 1] = (self.pow[i] * base) % mod

        def get(self, l, r):
            # 0-indexed, [l. r)
            return (self._hash[r] - self._hash[l] * self.pow[r - l]) % self.mod

    S = [ord(s) for s in input().rstrip('\n')]
    T = [ord(t) for t in input().rstrip('\n')]

    RH_S = RollingHash(S, 1007, 1000000007)
    RH_T = RollingHash(T, 1007, 1000000007)
    lt = len(T)
    T_hash = RH_T.get(0, lt)
    for i in range(len(S) - len(T) + 1):
        if RH_S.get(i, i+lt) == T_hash:
            print(i)


if __name__ == '__main__':
    main()

