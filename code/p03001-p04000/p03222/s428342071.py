###############################################################################

from bisect import bisect_left as binl

def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return map(int, input_tuple)


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


###############################################################################


def calc_bincount(w):
    bincount = {}
    for i in range(w - 1):
        bincount[i] = 2**i
        for j in range(2**i):
            while j:
                if j & 3 == 3:
                    bincount[i] -= 1
                    break
                j >>= 1
    bincount[-4] = bincount[-3] = bincount[-2] = bincount[-1] = 1
    return bincount


def main():
    h, w, k = intin()
    mod = 1000000007

    bincount = calc_bincount(w)

    counts_first = {}
    for i in range(1, w + 1):
        counts_first[i] = 0
    counts_first[1] = 1
    h_to_counts = {0: counts_first}

    for i in range(1, h + 1):
        prev_counts = h_to_counts[i - 1]
        h_to_counts[i] = {}
        for j in range(1, w + 1):
            h_to_counts[i][j] = 0

            # j - 1 --> j
            if j > 1:
                incr = ((bincount[j-3] * bincount[((w+1)-j)-2]) * prev_counts[j-1]) % mod
                h_to_counts[i][j] += incr
                h_to_counts[i][j] %= mod

            # j --> j
            incr = ((bincount[j-2] * bincount[((w+1)-j)-2]) * prev_counts[j]) % mod
            h_to_counts[i][j] += incr
            h_to_counts[i][j] %= mod

            # j + 1 --> j
            if j < w:
                incr = ((bincount[j-2] * bincount[((w+1)-j)-3]) * prev_counts[j+1]) % mod
                h_to_counts[i][j] += incr
                h_to_counts[i][j] %= mod

    print(h_to_counts[h][k])


if __name__ == '__main__':
    main()
