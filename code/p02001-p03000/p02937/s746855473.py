def main():
    S = input()
    T = input()
    N = len(S)

    def check(S, T):
        b = {s for s in S}
        for t in T:
            if t not in b:
                return True  # -1
        return False

    def is_ok(mid, now, ans):
        if ans < now[mid]:
            return True
        else:
            return False

    def binary_search_meguru(now, ans):
        ng = -1
        ok = len(now)-1
        while abs(ok - ng) > 1:
            mid = ng + (ok - ng) // 2
            if is_ok(mid, now, ans):
                ok = mid
            else:
                ng = mid
        return now[ok]

    if check(S, T):
        return print(-1)

    from string import ascii_lowercase

    dic = {a: [] for a in ascii_lowercase}
    for i, s in enumerate(S):
        dic[s].append(i+1)
    ans = 0
    cycle = 0
    for t in T:
        now = dic[t]
        if now[-1] <= ans:
            cycle += 1
            ans = 0
        idx = binary_search_meguru(now, ans)
        ans = idx
    print(ans + N*cycle)


if __name__ == '__main__':
    main()
