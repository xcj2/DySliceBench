def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1

    while first <= last:
        midpoint = (first + last)//2
        if item < alist[midpoint] and alist[midpoint - 1] < item or midpoint == 0 and item < alist[midpoint]:
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return -1


def load_input():
    n, k = list(map(int, input().split()))
    s = list(input())
    return n, k, s


def main():
    n, k, s = load_input()

    starts = [0]
    ends = []
    for i in range(n):
        if 0 < i and s[i - 1] == '1' and s[i] == '0':
            ends.append(i)

        if 0 < i and s[i - 1] == '0' and s[i] == '1':
            starts.append(i)
    ends.append(n)

    ml = 0
    for start in starts:
        order = k
        if start == 0 and s[0] == '0':
            order -= 1
        i = binarySearch(ends, start)
        if i + order < len(ends):
            end = ends[i + order]
        else:
            end = ends[-1]
        if ml < end - start:
            ml = end - start
    print(ml)


if __name__ == '__main__':
    main()