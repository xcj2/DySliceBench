def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def ok(W):
    if W.count("AGC") >= 1:
        return False

    for i in range(1, 4):
        L = list(W)
        L[i - 1], L[i] = L[i], L[i - 1]
        if "".join(L).count("AGC") >= 1:
            return False
    return True


def main():
    mod = 10 ** 9 + 7
    dp = {}
    W = "ACGT"
    for a in W:
        for b in W:
            for c in W:
                w = a + b + c
                if w in ("AGC", "ACG", "GAC"):
                    continue
                dp[w] = 1

    N = int(input())
    for n in range(N - 3):
        dp2 = {}
        for a in dp.keys():
            for b in W:
                if ok(a + b):
                    w = a[1:] + b
                    dp2[w] = (dp[a] + dp2.setdefault(w, 0)) % mod
        dp.update(dp2)
    print(sum(v for v in dp.values()) % mod)


if __name__ == "__main__":
    main()
