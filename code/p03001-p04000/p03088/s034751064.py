def solve():
    from functools import lru_cache

    mod = 10 ** 9 + 7

    def is_ok(last4: str) -> bool:
        if 'AGC' in last4:
            return False
        for j in range(3):
            t = list(last4)
            t[j], t[j + 1] = t[j + 1], t[j]
            if 'AGC' in ''.join(t):
                return False
        return True

    @lru_cache(maxsize=None)
    def dfs(curr: int = 0, last3: str = 'XXX'):
        ret = 0
        if curr == n:
            return 1
        for c in 'ACGT':
            last4 = last3 + c
            if is_ok(last4):
                ret += dfs(curr + 1, last4[1:])
        return ret % mod

    n = int(input())
    print(dfs())


solve()
