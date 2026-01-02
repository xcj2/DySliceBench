# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D


def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v


def shellSort(A, n):
    global cnt
    cnt = 0
    # sort period
    G = []
    h = 1
    while h <= len(A):
        G.append(h)
        h = h * 3 + 1
    G.reverse()

    m = len(G)
    for i in range(m):
        insertionSort(A, n, G[i])

    # output
    print(m)
    print(*G)
    print(cnt)
    print(*A, sep='\n')


def solve():
    m = int(input())
    A = [int(input()) for _ in range(m)]
    shellSort(A, m)


if __name__ == '__main__':
    solve()

