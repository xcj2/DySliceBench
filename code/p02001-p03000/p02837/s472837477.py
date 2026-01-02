# from math import sqrt
# from heapq import heappush, heappop
# from collections import deque
# from functools import reduce

# a, b = [int(v) for v in input().split()]


def main():
    N = int(input())

    table = []
    for _ in range(N):
        A = int(input())
        ary = []
        for _ in range(A):
            x, y = map(int, input().split())
            ary.append((x - 1, y))

        table.append(ary)

    def check(bit):
        for i in range(N):
            if (bit & (1 << i)) == 0:
                continue
            for x, y in table[i]:
                if y == 1 and bit & (1 << x) == 0:
                    return False
                if y == 0 and bit & (1 << x) != 0:
                    return False
        return True

    def search(i, bit):
        if i == N:
            if not check(bit):
                return 0
            return sum(1 for i in range(N) if (bit & (1 << i)) != 0)

        count1 = search(i + 1, bit)
        count2 = search(i + 1, bit | (1 << i))
        return max(count1, count2)

    count = search(0, 0)
    print(count)


main()
