

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def popcount(N):
    if N == 0:
        return 0
    one_count = 0
    temp = N
    while temp > 0:
        one_count += temp%2
        temp //= 2
    return 1+popcount(N%one_count)


def solve():
    N = read_int()
    X = input()
    one_count = X.count('1')
    if one_count == 0:
        for _ in range(N):
            print(1)
        return

    new_X = [0]*N
    steps = [0]*N

    base_up = 1
    up_under_modulo = 0

    for i in range(N-1, -1, -1):
        if X[i] == '1':
            up_under_modulo = (up_under_modulo+base_up)%(one_count+1)
        if X[i] == '0':
            new_X[i] += base_up
            steps[i] = 1
        base_up = (base_up*2)%(one_count+1)

    base_down = 1
    down_under_modulo = 0

    if one_count > 1:
        for i in range(N-1, -1, -1):
            if X[i] == '1':
                down_under_modulo = (down_under_modulo+base_down)%(one_count-1)
            if X[i] == '1':
                new_X[i] -= base_down
                steps[i] = 1
            base_down = (base_down*2)%(one_count-1)

    for i in range(N):
        if X[i] == '1':
            if one_count > 1:
                new_X[i] = (new_X[i]+down_under_modulo)%(one_count-1)
        else:
            new_X[i] = (new_X[i]+up_under_modulo)%(one_count+1)

    for i in range(N):
        print(steps[i]+popcount(new_X[i]))


if __name__ == '__main__':
    solve()
