

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def bit_indexes(x):
    i = 0
    while x != 0:
        if x%2 != 0:
            yield i
        x //= 2
        i += 1
    

def solve():
    H, W, K = read_ints()
    C = []
    black_count = 0
    for i in range(H):
        C.append(input().strip())
        black_count += C[-1].count('#')
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            count = black_count
            for i0 in bit_indexes(i):
                for j0 in range(W):
                    if C[i0][j0] == '#':
                        count -= 1
            for j0 in bit_indexes(j):
                for i0 in range(H):
                    if C[i0][j0] == '#':
                        count -= 1
            for i0 in bit_indexes(i):
                for j0 in bit_indexes(j):
                    if C[i0][j0] == '#':
                        count += 1
            if count == K:
                ans += 1
    return ans


if __name__ == '__main__':
    print(solve())
