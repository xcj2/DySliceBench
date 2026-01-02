def solve():
    p = read()
    result = think(p)
    write(result)


def read():
    n = read_int(1)[0]
    return read_float(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(p):
    n = len(p)

    # dp[ith coin frip trial][faces count] = prob
    # dp[ith][facecount] = dp[ith - 1][facecount - 1] * Phead + dp[ith - 1][facecount] * Ptail

    accumulated = [[0.0 for x in range(n + 1)] for y in range(n)]
    accumulated[0][0] = 1.0 - p[0]
    accumulated[0][1] = p[0]

    for ith, each_p in enumerate(p):
        if ith == 0:
            continue
        for face_count in range(ith + 2):
            if face_count == 0:
                accumulated[ith][face_count] = accumulated[ith - 1][face_count] * (1.0 - each_p)
            elif face_count == ith + 1:
                accumulated[ith][face_count] = accumulated[ith - 1][face_count - 1] * each_p
            else:
                accumulated[ith][face_count] = accumulated[ith - 1][face_count] * (1.0 - each_p) + accumulated[ith - 1][face_count - 1] * each_p

    return sum(accumulated[n - 1][((n + 1) // 2):])


def write(result):
    print(result)


if __name__ == '__main__':
    solve()