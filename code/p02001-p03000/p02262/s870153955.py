def main():
    n = int(input())
    numbers = [int(input()) for i in range(n)]
    count = shellSort(numbers, n)

    print(count)
    [print(i) for i in numbers]

def shellSort(numbers, n):
    count = 0
    m = 1
    g = []
    while m <= n :
        g.append(m)
        m = 3 * m + 1
    g.reverse()
    for h in g:
        count += insertionSort(numbers, n, h)

    print(len(g))
    print(' '.join(map(str, g)))

    return count

def insertionSort(numbers, n, h):
    count = 0
    for i in range(h, n, 1):
        v = numbers[i]
        j = i - h
        while (j >= 0) & (numbers[j] > v):
            numbers[j + h] = numbers[j]
            j -= h
            count += 1

        numbers[j + h] = v

    return count

if __name__ == '__main__':
    main()

