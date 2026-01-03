

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    A, B = [], []
    for _ in range(N):
        A.append(input())
    for _ in range(M):
        B.append(input())
    for i in range(N-M+1):
        for j in range(N-M+1):
            matches = True
            for i0 in range(i, i+M):
                for j0 in range(j, j+M):
                    if A[i0][j0] != B[i-i0][j-j0]:
                        matches = False
                        break
                if not matches:
                    break
            if matches:
                return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(solve())
