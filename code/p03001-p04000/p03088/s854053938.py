def main():
    from functools import lru_cache
    N = int(input())
    MOD = 10**9 + 7

    def is_ok(last4):
        for i in range(4):
            t = list(last4)
            if i >= 1:
                t[i-1], t[i] = t[i], t[i-1]
            if "".join(t).count("AGC") >= 1:
                return False
        return True

    @lru_cache(maxsize=10000)
    def dfs(cur, last3):
        if cur == N:
            return 1
        ret = 0
        for c in "AGCT":
            if is_ok(last3 + c):
                ret = (ret + dfs(cur + 1, last3[1:] + c)) % MOD
        return ret

    print(dfs(0, "TTT"))


if __name__ == '__main__':
    main()
