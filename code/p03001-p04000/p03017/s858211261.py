import sys

def InputToInt():
    A = input().split()
    for i in range(len(A)):
        A[i] = int(A[i])
    return A


def Yes():
    print('Yes')
    sys.exit()


def No():
    print('No')
    sys.exit()


if __name__ == '__main__':
    N, A, B, C, D = InputToInt()
    L = input()
    if D > C:
        for i in range(A, D-2):
            if L[i:i+2] == '##':
                No()
        Yes()

    if D < C:
        for i in range(A, C-2):
            if L[i:i+2] == '##':
                No()
        if '...' in L[B-2:D+1]:
            Yes()
        else:
            No()
                