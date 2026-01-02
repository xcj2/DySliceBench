def insertionSort(a, n, g):
    cnt = 0

    for i in range(g, n):
        v = a[i]
        j = i - g

        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j - g
            cnt += 1

        a[j+g] = v

    return (cnt, a)

def shellSort(a, n):
    cnt = 0

    for i in g(n):
        c, a = insertionSort(a, n, i)
        cnt += c

    return (cnt, a)

def g(n):
    nums = []

    h = 1
    while True:
        nums.append(h)
        h = 3*h+1

        if n < h:
            break

    return list(reversed(nums))

def main():
    n = int(input())

    a = []
    for _ in range(n):
        a.append(int(input()))

    G = g(n)
    cnt, a = shellSort(a, n)

    print(len(G))
    print(' '.join([str(x) for x in G]))
    print(cnt)
    for x in a:
        print(x)

if __name__ == '__main__':
    main()

