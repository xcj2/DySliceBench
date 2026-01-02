

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def manhattan(p0, p1):
    return abs(p0[0]-p1[0])+abs(p0[1]-p1[1])


def solve():
    """
    """
    H, W, D = read_ints()
    arr = [None for _ in range(H*W)]
    for i in range(H):
        for j, a in enumerate(read_ints()):
            arr[a-1] = (i, j)
    prefix = [0]*(H*W)
    for i in range(D):
        for j in range(i+D, H*W, D):
            prefix[j] = prefix[j-D]+manhattan(arr[j], arr[j-D])
    Q = read_int()
    for _ in range(Q):
        l, r = read_ints()
        print(prefix[r-1]-prefix[l-1])




if __name__ == '__main__':
    solve()
