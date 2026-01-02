H, W, K = map(int, input().split())


def pattern(n):
    if n < 1:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return pattern(n-2) + pattern(n-1)


def memorize(func):
    cache = {}

    def inner(*args):
        if args in cache:
            return cache[args]
        else:
            ret = func(*args)
            cache[args] = ret
            return ret

    return inner


@memorize
def count(h, W, K):
    if h == 0:
        if K == 1:
            return 1
        else:
            return 0
    ret = 0
    if 1 < K:
        ret += count(h-1, W, K-1) * pattern(K-3) * pattern(W-K-1)
    ret += count(h-1, W, K) * pattern(K-2) * pattern(W-K-1)
    if K < W:
        ret += count(h-1, W, K+1) * pattern(K-2) * pattern(W-K-2)
    return ret


print(count(H, W, K) % 1000000007)