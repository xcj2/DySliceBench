class BinaryIndexedTree(object):
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)

    def bit_add(self, index, num):
        while (index <= self.N):
            self.bit[index] += num
            index += index & -index
        return

    def bit_sum(self,index):
        result = 0
        while (index > 0):
            result += self.bit[index]
            index -= index & -index
        return result

    def bit_sum_range(self, l, r):
        if (l == r):
            return 1
        else:
            return self.bit_sum(r) - self.bit_sum(l - 1)

def main():
    from sys import stdin
    N, Q = list(map(int, input().split()))
    c = list(map(int, input().split()))
    readline = stdin.readline
    query = [list(map(int, readline().split())) + [i] for i in range(Q)]
    query_result = [0 for i in range(Q)]
    collar_pos = [-1] * (N + 1)
    bit = BinaryIndexedTree(N)

    sorted_query = sorted(query, key=lambda query: query[1])

    index = 1
    for query in sorted_query:
        l, r, q = query
        while (index <= r):
            # update BIT
            if (collar_pos[c[index-1]] != -1):
                bit.bit_add(collar_pos[c[index-1]], -1)
            bit.bit_add(index, 1)
            # update collar_pos
            collar_pos[c[index-1]] = index
            index += 1
        query_result[q] = bit.bit_sum_range(l, r)

    print(*query_result, sep='\n')

if __name__ == '__main__':
    main()