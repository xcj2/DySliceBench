def mark(a, b):
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                a[i][j] = 0


def check_h(a):
    for row in a:
        if row == [0, 0, 0]:
            return True


def check_v(a):
    for col in range(3):
        if [row[col] for row in a] == [0, 0, 0]:
            return True


def check_c(a):
    if [a[i][i] for i in range(3)] == [0, 0, 0] or [a[i][2 - i] for i in range(3)] == [0, 0, 0]:
        return True


def resolve():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    for _ in range(N):
        B = int(input())
        mark(A, B)
    if check_h(A) or check_v(A) or check_c(A):
        print("Yes")
    else:
        print("No")
resolve()