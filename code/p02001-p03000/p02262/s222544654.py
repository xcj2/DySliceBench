def main():
    n = int(input())
    array = [int(input()) for _ in range(n)]
    count = 0
    gs = make_margins(n)
    m = len(gs)
    for g in gs:
        count += insertionSort(array, n, g)
    print(m)
    print(' '.join(map(str, gs)))
    print(count)
    for e in array:
        print(e)


def make_margins(n):
    gs = [1]
    while 3*gs[-1] + 1 < n:
        gs.append(3*gs[-1] + 1)
    return list(reversed(gs))


def insertionSort(array, n, g):
    cnt = 0
    for i in range(g, n):
        v = array[i]
        j = i - g
        while j >= 0 and array[j] > v:
            array[j+g] = array[j]
            j = j - g
            cnt += 1
        array[j+g] = v
    return cnt


if __name__ == '__main__':
    main()

