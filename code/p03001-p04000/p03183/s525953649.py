

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    assume s1 was bottom
    s1-w0 > s0-w1 better solidness
    s1+w1 > s0+w0
    otherwise
    s1+w1 < s0+w0

    OPT[i][j] - maximum value up to i-th brick with weight j
    OPT[i][j] = OPT[i-1][j-w[i]]+v[i] if we take i-th brick, 0 <= j-w[i] <= s[i]
                OPT[i-1][j]
    OPT[0][w[0]] = v[0], otherwise OPT[0][j] = 0
    """
    N = read_int()
    pairs = []
    max_w = 0
    max_s = 0
    for _ in range(N):
        w0, s0, v0 = read_ints()
        max_w = max(max_w, w0)
        max_s = max(max_s, s0)
        pairs.append((s0+w0, w0, s0, v0))
    MAX_WEIGHT = max_w+max_s+1
    pairs.sort()
    OPT = [
        [0]*MAX_WEIGHT for _ in range(N)
    ]
    OPT[0][pairs[0][1]] = pairs[0][3]
    for i in range(1, N):
        for j in range(MAX_WEIGHT):
            OPT[i][j] = max(OPT[i][j], OPT[i-1][j])
            if 0 <= j-pairs[i][1] <= pairs[i][2]:
                OPT[i][j] = max(OPT[i][j], OPT[i-1][j-pairs[i][1]]+pairs[i][3])
    return max(OPT[-1])


if __name__ == '__main__':
    print(solve())
