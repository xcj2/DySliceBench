import numpy as np

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


def main():
    N = ii()
    A = lii()
    for i in range(N):
        A[i] -= (i + 1)

    A = np.array(sorted(A))
    offset = A[0]
    A = A - offset
    s1 = A.sum()
    mins = s1
    s2 = 0
    nowv = 0

    for i, v in enumerate(A):
        if nowv < v:
            s1 -= (v - nowv) * (N - i)
            s2 += (v - nowv) * i
            nowv = v
            if s1 + s2 < mins:
                mins = s1 + s2

    return mins

if __name__ == '__main__':
    print(main())