# Reference: https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree
class BinaryIndexedTree:
    # a = [0] * n
    def __init__(self, n):
        self.size = n
        self.data = [0] * (n+1)

    # return sum(a[0:i])
    def cumulative_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.data[i]
            i -= i & -i
        return ans

    # a[i] += x
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.data[i] += x
            i += i & -i

from sys import stdin
input = stdin.buffer.readline

def main():
    n, q = map(int, input().split())
    c = list(map(int, input().split()))

    lis = [[] for _ in range(n + 1)]
    for i, ci in enumerate(c):
        lis[ci].append(i)

    BIT = BinaryIndexedTree(n)
    for i in range(n+1):
        if len(lis[i]) > 0:
            BIT.add(lis[i].pop(-1), 1)

    query = [0] * q
    ans = [-1] * q
    for lap in range(q):
        l, r = map(int, input().split())
        query[lap] = (l-1, r, lap)
    
    query.sort(reverse=True, key=lambda x: x[1])

    now_r = n
    for ind, (l, r, lap) in enumerate(query):
        while now_r > r:
            now_r -= 1
            BIT.add(now_r, -1) # delete
            if len(lis[c[now_r]]) > 0:
                BIT.add(lis[c[now_r]].pop(-1), 1) # add
        ans[lap] = BIT.cumulative_sum(r) - BIT.cumulative_sum(l)
    
    for i in ans:
        print(i)

main()
