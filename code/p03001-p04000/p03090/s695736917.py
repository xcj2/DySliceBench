

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    table = [
        [1 for _ in range(N)] for _ in range(N)
    ]
    if N%2 == 0:
        for i in range(N//2):
            table[i][N-i-1] = table[N-i-1][i] = 0
    else:
        for i in range(N//2):
            table[i][N-i-2] = table[N-i-2][i] = 0
    size = 0
    answer = []
    for i in range(N):
        for j in range(i+1, N):
            if table[i][j]:
                answer.append((i+1, j+1))
                size += 1
    print(size)
    for a in answer:
        print(*a)


if __name__ == '__main__':
    solve()
