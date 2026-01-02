

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[K] - answers if Taro wins with K stones

    OPT[a[i]] = True 1 <= k <= N

    5
    2 3
    
    t t j j j
    t t t j j

    OPT(K) - True, if Taro loses the game with K stones
    OPT(K) = all(not OPT(K-a[i])) 1 <= i <= N
    OPT(0) = True
    """
    N, K = read_ints()
    a = read_ints()
    OPT = [False]*(K+1)
    OPT[0] = True
    for k in range(1, K+1):
        OPT[k] = all(not OPT[k-a[i]] for i in range(N) if k-a[i] >= 0)
    if OPT[K]:
        return 'Second'
    return 'First'


if __name__ == '__main__':
    print(solve())
