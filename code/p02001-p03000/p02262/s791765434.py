cnt = 0


def insertion_sort(a, n, g):
    global cnt
    for i in range(g, n):
        v = a[i]
        j = i-g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j-g
            cnt += 1
        a[j+g] = v


def shell_sort(a, n):
    g = [1]
    for i in range(100):
        if g[-1]*3+1 < n:
            g.append(g[-1]*3+1)
    g.reverse()
    m = len(g)
    print(m)
    print(' '.join(map(str, g)))
    for i in range(m):
        insertion_sort(a, n, g[i])


def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    shell_sort(a, n)
    print(cnt)
    for i in a:
        print(i)


if __name__ == "__main__":
    main()

