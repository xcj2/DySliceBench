import numpy as np

N, K = list(map(int, input().split()))

x = list(map(int, input().split()))


def calc(m, n, default=100000000):
    tmp = 0
    if m > n:
        tmp = m + 2*n
    else:
        tmp = 2*m + n

    min = tmp if default > tmp else default

    return min


def my_index(l, i, default=False):
    if i in l:
        return True
    else:
        return default


def main():
    global x, K
    if 0 in x:
        K -= 1
        if K == 0:
            return 0

    x = np.array(x)
    positives = x[np.where(x > 0)]
    negatives = x[np.where(x < 0)]

    nega_size = np.size(negatives)
    posi_size = np.size(positives)
    if nega_size == 0:
        return positives[K-1]

    if posi_size == 0:
        return abs(negatives[-K])

    if K <= nega_size and K <= posi_size:
        min = 1e9
        for i in range(K+1):
            if i == 0:
                min = abs(negatives[-K])
            elif i > 0 and i < K:
                ne = abs(negatives[-K+i])
                po = positives[i-1]
                min = calc(ne, po, min)
            elif i == K:
                tmp = positives[K-1]
                min = tmp if min > tmp else min

        return min

    if K > nega_size and K > posi_size:
        min = 1e9
        for i in range(N-K+1):
            ne = abs(x[i])
            po = x[K+i-1]
            min = calc(ne, po, min)

        return min

    if nega_size < K and K <= posi_size:
        min = 1e9
        for i in range(nega_size):
            po = x[K+i-1]
            ne = abs(x[i])
            min = calc(ne, po, min)

        min = abs(positives[K-1]) if abs(positives[K-1]) < min else min
        return min

    if posi_size < K and K <= nega_size:
        min = 1e9
        for i in range(posi_size):
            po = x[-i-1]
            ne = abs(x[-K-i])
            min = calc(po, ne, min)

        min = abs(negatives[-K]) if abs(negatives[-K]) < min else min
        return min


print(main())
