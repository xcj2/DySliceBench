def solve():
    import sys
    input = sys.stdin.readline

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


    N, Q = map(int, input().split())
    *c, = map(int, input().split())
    tree = FenwickTree(N+1)
    m = [tuple(map(int, input().split()))+(i,) for i in range(Q)]
    m.sort(key=lambda x:x[1])

    right = 0
    pos = [-1] * (N+1)
    ans = [None] * (Q)

    for l, r, idx in m:
        for i in range(right, r):
            x = pos[c[i]]
            if x != -1:
                tree.add(x, -1)
            pos[c[i]] = i+1
            tree.add(i+1, 1)
        ans[idx] = tree.rangesum(l, r)
        right = r
    for i in ans:
        print(i)


solve()
