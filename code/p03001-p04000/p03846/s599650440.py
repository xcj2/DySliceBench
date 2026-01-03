MOD = 10**9+7


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def pow(b, p):
    ans = 1
    for _ in range(p):
        ans = (ans*b)%MOD
    return ans


def solve():
    """
    if N is odd, 
    N-1 : 2
    N-3 : 2
    0   : 1
    if N is even,
    N-1 : 2
    N-3 : 2
    1   : 1


    1 2 3 4 5 6
    1 2 3 4 5
    """
    N = read_int()
    A = read_ints()
    D = [0]*((N+1)//2)
    if N%2 == 0:
        for a in A:
            if a%2 == 0:
                return 0
            if a >= N:
                return 0
            if D[a//2] == 2:
                return 0
            D[a//2] += 1
    else:
        for a in A:
            if a%2 == 1:
                return 0
            if a >= N:
                return 0
            if D[a//2] == 2:
                return 0
            if D[0] == 2:
                return 0
            D[a//2] += 1
    return pow(2, N//2)


if __name__ == '__main__':
    print(solve())
