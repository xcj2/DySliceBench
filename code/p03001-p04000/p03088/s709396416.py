from functools import lru_cache


def check(s):
    bads = ["AGC", "ACG", "GAC"] + [b.format(_s) for b in ["AG{}C", "A{}GC"] for _s in "ACGT"]
    return not any(map(lambda x: x in s, bads))


def solve(string):
    n = int(string)

    @lru_cache(n * 4**3)
    def dfs(pos, last3):
        if pos == n:
            return 1
        ans = 0
        for _s in "ACGT":
            ans += dfs(pos + 1, last3[1:] + _s) if check(last3 + _s) else 0
        return ans % (10**9 + 7)

    return str(dfs(0, "TTT"))


if __name__ == '__main__':
    print(solve(input()))
