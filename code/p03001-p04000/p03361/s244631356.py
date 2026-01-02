import numpy as np
na = np.array

def ii():
    return int(input())


def lii():
    return list(map(int, input().split(' ')))


def lvi(N):
    l = []
    for _ in range(N):
        l.append(ii())
    return l


def lv(N):
    l = []
    for _ in range(N):
        l.append(input())
    return l


def yn(b):
    if b:
        print('Yes')
    else:
        print('No')


def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


def ok(S, i, j):
    try:
        if S[i+1][j] == '#':
            return True
    except:
        pass
    try:
        if S[i-1][j] == '#':
            return True
    except:
        pass
    try:
        if S[i][j+1] == '#':
            return True
    except:
        pass
    try:
        if S[i][j-1] == '#':
            return True
    except:
        pass

    return False


def C():

    H, W = lii()
    S = []
    for _ in range(H):
        S.append(input())

    for i, l in enumerate(S):
        for j in range(len(l)):
            if S[i][j] == '#':
                if not ok(S, i, j):
                    return False

    return True


if __name__ == '__main__':
    yn(C())