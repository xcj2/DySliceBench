
def bubblesort(n, a):
    r = a[:]
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(r[j][1]) < int(r[j-1][1]):
                r[j], r[j-1] = r[j-1], r[j]

    print(*r)
    print("Stable")


def selectionsort(n, a):
    r = a[:]
    ret = "Stable"
    for i in range(n):
        tmp = i
        for j in range(i, n):
            if int(r[j][1]) < int(r[tmp][1]):
                tmp = j
        r[i], r[tmp] = r[tmp], r[i]

    for i in range(n):
        for j in range(i+1, n):
            for k in range(n):
                for l in range(k+1, n):
                    if int(a[i][1]) == int(a[j][1]) and a[i] == r[l] and a[j] == r[k]:
                        ret = "Not stable"

    print(*r)
    print(ret)


def main():
    n = int(input())
    a = list(input().split())

    bubblesort(n, a)
    selectionsort(n, a)


if __name__ == '__main__':
    main()
