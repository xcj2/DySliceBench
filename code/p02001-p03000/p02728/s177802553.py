class Combination():
    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1]*(n+1)
        for i in range(1,n+1):
            self.fac[i] = self.fac[i-1] * i % self.mod
        self.invfac = [1]*(n+1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n-1, 0, -1):
            self.invfac[i] = self.invfac[i+1] * (i+1) % self.mod
    
    def combination(self, n, r):
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod
    
    def factorial(self, i):
        return self.fac[i]
    
    def invfactorial(self, i):
        return self.invfac[i]


class Rerooting(Combination):
    def __init__(self, adjacent, n, mod):
        super(Rerooting, self).__init__(n, mod)
        self.n = n
        self.adj = adjacent   # 0-indexedの配列で用意！
        # DFSで行きがけ順を記録
        self.order = []
        stack = [0]
        self.parent = [-1]*(n)
        while stack:
            node = stack.pop()
            self.order.append(node)
            for child in self.adj[node]:
                if self.parent[node] == child:
                    continue
                stack.append(child)
                self.parent[child] = node
    
    def merge(self, parent, child):
        # childの値をparentに統合する処理
        self.size[parent] += self.size[child]
        self.dp[parent] *= self.combination(self.size[parent]-1,self.size[child])
        self.dp[parent] %= self.mod
        self.dp[parent] *= self.dp[child]
        self.dp[parent] %= self.mod
        return self.dp[parent]

    def remerge(self, parent, child):
        # childの値が根となるときの統合処理
        self.dp[child] = self.size[child]*self.dp[parent]
        self.dp[child] *= pow(self.n-self.size[child], self.mod -2, self.mod)
        self.dp[child] %= self.mod
        return self.dp[child]

    def calc_subtree(self):
        # 帰りがけ順で木DPを行う
        # 根が0の時の値を算出
        self.dp = [1]*(self.n)
        self.size = [1]*(self.n)
        for node in self.order[::-1]:
            if self.parent[node] == -1:
                continue
            self.merge(self.parent[node], node)

    def root_subtree(self):
        # 行きがけ順で
        for node in self.order[1:]:
            p = self.parent[node]
            self.remerge(p, node)
        return self.dp
        

def main():
    import sys
    input = lambda: sys.stdin.buffer.readline().rstrip()
    n = int(input())
    mod = 10**9 + 7
    adj = [[] for i in range(n)]
    for i in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        adj[a].append(b)
        adj[b].append(a)

    r = Rerooting(adj, n, mod)
    r.calc_subtree()
    dp = r.root_subtree()

    for ans in dp:
        print(ans)


if __name__ == '__main__':
    main()