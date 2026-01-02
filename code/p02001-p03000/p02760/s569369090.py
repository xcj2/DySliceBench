def create_hole(A: list, b:list):

    N = len(A)
    Hole = [[0 for i in range(N)] for j in range(N)]
    for i in range(3):
        for j in range(3):
            for value in b:
                if A[i][j] == value: Hole[i][j] = 1

    return Hole


def check_bingo(H: list):

    N = len(H)
    rowsum = sum([sum(row) == N for row in H])
    colsum = sum([sum(row) == N for row in map(list, zip(*H))])
    digsum = sum([H[i][i] for i in range(N)]) == N
    tdigsum = sum([H[i][N-i-1] for i in range(N)]) == N

    return rowsum + colsum + digsum + tdigsum > 0


def resolve():

    A = [list(map(int, input().split())) for i in range(3)]
    N = int(input())
    b = [int(input()) for i in range(N)]
    print('Yes' if check_bingo(create_hole(A, b)) else 'No')
    
resolve()