#  --*-coding:utf-8-*--

def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper


@memoize
def f(d, k):
    if d == 1:
        return 1

    s = f(d-1, k)

    if k > 0:
        s += f(d-1, k-1)

    if k < 9:
        s += f(d-1, k+1)

    return s


def g1(K):
    d = 1
    cnt = 0

    while True:
        for i in range(1, 10):
            cnt2 = f(d, i)
            if (cnt + cnt2 >= K):
                return (cnt, d, i)

            cnt += cnt2

        d += 1


def g2(K, cnt, d, k):
    d -= 1
    X = [k]

    while d > 0:
        for j in range(-1, 2):
            if k+j < 0 or k+j > 9:
                continue

            cnt2 = f(d, k+j)

            if (cnt + cnt2 >= K):
                X.append(k+j)
                k = k+j
                break

            cnt += cnt2

        d -= 1

    return X

K = int(input())
cnt, d, k = g1(K)
print(''.join(map(str, g2(K, cnt , d, k))))

