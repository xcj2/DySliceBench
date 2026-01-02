

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    S = []
    twos = 1
    sign = 1
    while N != 0:
        if N%(2*twos) != 0:
            S.append('1')
            if sign < 0:
                N += twos
            else:
                N -= twos
        else:
            S.append('0')
        sign = -sign
        twos *= 2
    if len(S) == 0:
        S = ['0']
    S.reverse()
    print(''.join(S))


if __name__ == '__main__':
    solve()
