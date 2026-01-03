import sys

class BIT(object):
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def sum(self, i):
        cumulative_sum = 0
        while i > 0:
            cumulative_sum += self.data[i]
            i -= i & (-i)
        return cumulative_sum

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & (-i)
        return

def main():
    N, K = map(int, input().split())
    A_list = [int(input()) for i in range(N)]

    cumulative_sum = 0
    b_list = [(0, 0)]
    for i, i_A in enumerate(A_list, 1):
        cumulative_sum += i_A
        b_list.append((cumulative_sum - K*(i), i))

    b_list.sort()
    compression_number = 1
    c_list = [None]*(N+1)
    for _, i in b_list:
        c_list[i] = compression_number
        compression_number += 1

    bit = BIT(N+1)
    ans = 0
    for i_c in c_list:
        ans += bit.sum(i_c)
        bit.add(i_c, 1)

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)