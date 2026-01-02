def show(A, n):
    for i in range(n):
        print(A[i])


def insertion_sort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v


def shell_sort(A, n):
    global cnt
    cnt = 0

    G = []
    g = 1
    while g <= n:
        G.append(g)
        g = 3 * g + 1

    print(len(G))
    for g in reversed(G):
        if g != 1:
            print(g, end=' ')
        else:
            print(g)
        insertion_sort(A, n, g)
    print(cnt)
    show(A, n)


def main():
    n = int(input())
    A = [int(input()) for i in range(n)]

    shell_sort(A, n)


if __name__ == "__main__":
    main()

