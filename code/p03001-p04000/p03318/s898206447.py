def d_snuke_numbers(K):
    import math

    def ns(n):  # n/S(n)の計算
        return n / sum(map(int, list(str(n))))

    def f(n):  # n<=xの中で ns(x) を最小にするような最小の値xを求める
        digit = len(str(n))
        # n自身も候補の1つである
        min_ns = ns(n)
        ret = n
        for d in range(digit + 1):
            x = (10**(d+1)) * math.floor(n / (10**(d+1)) + 1) - 1
            s = ns(x)
            if min_ns > s:
                min_ns = s
                ret = x
        return ret

    n = 0
    candidate = []
    for _ in range(K):
        n = f(n + 1)
        candidate.append(n)
    ans = '\n'.join(map(str, candidate))
    return ans

K = int(input())
print(d_snuke_numbers(K))