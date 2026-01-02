

class FenwickTree:

    def __init__(self, size):
        self.size = size
        self.array = [0]*size

    def add(self, index, value):
        while index < self.size:
            self.array[index] += value
            index += index&(-index)

    def sum(self, index):
        answer = 0
        while index > 0:
            answer += self.array[index]
            index -= index&(-index)
        return answer

    def rangesum(self, start, end):
        return self.sum(end)-self.sum(start-1)


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().split(' ')))

def read_query():
    l, r = read_ints()
    return l-1, r-1

def solve():
    N, Q = read_ints()
    C = [c-1 for c in read_ints()]
    colour_to_index = [-1]*N
    queries = [read_query() for _ in range(Q)]
    answer = [-1]*Q
    queries_sorted_index = sorted(list(range(Q)), key=lambda i: queries[i][1])
    fenwick_tree = FenwickTree(N+1)
    last_r = -1
    for i in queries_sorted_index:
        l, r = queries[i]
        for j in range(last_r+1, r+1):
            colour = C[j]
            if colour_to_index[colour] != -1:
                fenwick_tree.add(colour_to_index[colour]+1, -1)
            colour_to_index[colour] = j
            fenwick_tree.add(colour_to_index[colour]+1, 1)
        answer[i] = fenwick_tree.rangesum(l+1, r+1)
        last_r = r
    print(*answer, sep='\n')


if __name__ == '__main__':
    solve()
