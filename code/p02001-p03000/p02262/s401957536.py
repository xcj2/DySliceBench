cnt = 0


def insertion_sort(a, n, g):
    global cnt
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j - g
            cnt += 1
            a[j+g] = v


def shell_sort(a, n):
    g = [1]
    while True:
        tmp = g[-1] * 3 + 1
        if tmp > n:
            break
        else:
            g.append(tmp)
    g.reverse()
    m = len(g)
    print(m)
    print(' '.join(map(lambda x: str(x), g)))
    for i in range(m):
        insertion_sort(a, n, g[i])


def main():
    global cnt
    a = [int(input()) for _ in range(int(input()))]
    shell_sort(a, len(a))
    print(cnt)
    print('\n'.join(map(lambda x: str(x), a)))


if __name__ == '__main__':
    main()

