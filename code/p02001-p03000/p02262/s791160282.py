def insertionSort(A, n, g, cnt):
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

    return cnt


def shellSort(A, n):
    cnt = 0

    G = []
    G.append(1)
    for i in range(n):
        tmp = 3 * G[-1] + 1
        if tmp > n:
            break
        else:
            G.append(tmp)
    G.reverse()
    m = len(G)

    print(m)
    print(*G)

    for i in range(m):
        cnt = insertionSort(A, n, G[i], cnt)

    print(cnt)


def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    shellSort(a, n)

    for i in range(n):
        print(a[i])


if __name__ == '__main__':
    main()
