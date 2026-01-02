import sys
input=sys.stdin.readline


class SegTree():
    def __init__(self, N, e, operator_func):
        self.e = e # 単位元
        self.size = N
        self.node = [self.e] * (2*N)
        self.operator_func = operator_func # 処理(add or xor max minなど)

    def set_list(self, l):
        for i in range(self.size):
            self.node[i+self.size-1] = l[i]
        for i in range(self.size-1)[::-1]:
            self.node[i] = self.operator_func(self.node[2*i+1], self.node[2*i+2])
    
    def update(self, k, x):
        k += self.size-1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self.operator_func(self.node[2*k+1], self.node[2*k+2])

    def get(self, l, r):
        # [l, r) についてqueryを求める
        x = self.e
        l += self.size
        r += self.size

        while l<r:
            if l&1:
                x = self.operator_func(x, self.node[l-1])
                l += 1
            if r&1:
                r -= 1
                x = self.operator_func(x, self.node[r-1])
            l >>= 1
            r >>= 1
        return x


def solve():
    N = int(input())
    l = [tuple(map(int, input().split())) for i in range(N)]
    l.sort(key=lambda x:(x[0], -x[1]))

    #1 [lmax, rmin] [*, *]
    #2 [lmax, *] [*, rmin]

    lmax = 0
    rmin = 10**12
    a, b = 0, 0

    for i in range(N):
        if lmax < l[i][0]:
            lmax = l[i][0]
            a = i
        if rmin > l[i][1]:
            rmin = l[i][1]
            b = i

    #1
    ans1 = 0
    for i in range(N):
        if i==a or i==b:
            continue
        ans1 = max(ans1, max(l[b][1]-l[a][0]+1, 0)+max(l[i][1]-l[i][0]+1, 0))

    #2
    ans2 = 0
    tree = SegTree(N, 10**12, min)
    tree.set_list([i[1] for i in l])
    for i in range(N-1):
        ans2 = max(ans2, max(l[b][1]-l[i][0]+1, 0)+max(tree.get(i+1, N)-l[a][0]+1, 0))

    ans = max(ans1, ans2)
    print(ans)


if __name__ == "__main__":
    solve()
