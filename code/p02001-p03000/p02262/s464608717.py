def generate_G(n):
    h = 1
    G = []
    while h <= n:
        G.append(h)
        h = 3 * h + 1
    G.reverse()
    return G


def insertion_sort(A, n, g):
    global count
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            count += 1
        A[j + g] = v


def shell_sort(A, n):
    G = generate_G(n)
    print(len(G))
    print(' '.join(map(str, G)))
    for g in G:
        insertion_sort(A, n, g)


def main():
    global count

    # input
    n = int(input())
    A = [int(input()) for _ in range(n)]

    # sort
    shell_sort(A, n)

    # output
    print(count)
    for a in A:
        print(a)


if __name__ == "__main__":
    count = 0
    main()

