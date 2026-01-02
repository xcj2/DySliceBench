class ReRooting(object):
    """ 全方位木DP """
    def processing(self, in_:list, v:int):
        """ 単項演算(加工) f """
        cnt = in_[0] * factinv[in_[1]] % MOD
        size = in_[1]
        return [cnt, size]
    
    def merge(self, in1:list, in2:list):
        """ 二項演算(マージ) ・ """
        cnt = in1[0] * in2[0] % MOD
        size = in1[1] + in2[1]
        return [cnt, size]

    def adjustment(self, in_:list, v:int):
        """ 単項演算(調整) g """
        cnt = in_[0] * fact[in_[1]] % MOD
        size = in_[1] + 1
        return [cnt, size]
    
    def solve(self):
        """
        計算結果を返す
        
        Ex. [cnt for cnt, _ in self.calc()]
        """
        return [cnt for cnt,_ in self.calc()]

    def __init__(self, V:int, e:list):
        """
        V: 頂点数
        e: 単位元
        """
        self.V, self.e = V, e
        self.edge = [[] for _ in range(V)]
        self.par = [-1] * V
        self.order = []
    
    def add_edge(self, u:int, v:int):
        """ 辺(u,v)をグラフに追加する """
        self.edge[u].append(v)
        self.edge[v].append(u)
    
    def topological_sort(self, root:int = 0):
        """ トポロジカルソート """
        from collections import deque
        que = deque([root])
        while que:
            v = que.popleft()
            self.order.append(v)
            for w in self.edge[v]:
                if w != self.par[v]:
                    self.par[w] = v
                    self.edge[w].remove(v)
                    que.append(w)
    
    def bottom_up(self):
        """ Bottom-Up DP """
        accBU = [self.e for _ in range(self.V)]
        resBU = [None] * self.V
        for v in reversed(self.order):
            for c in self.edge[v]:
                accBU[v] = self.merge(accBU[v], self.processing(resBU[c], c))
            resBU[v] = self.adjustment(accBU[v], v)
        return accBU, resBU
    
    def top_down(self, resBU:list):
        """ Top-Down DP """
        accTD = [self.e for _ in range(self.V)]
        resTD = [self.e for _ in range(self.V)]

        for p in self.order:
            ac = self.e if (p == self.order[0]) else self.processing(resTD[p], p)
            for v in self.edge[p]:
                accTD[v] = ac[:]
                ac = self.merge(ac, self.processing(resBU[v], v))
            
            ac = self.e
            for v in reversed(self.edge[p]):
                accTD[v] = self.merge(accTD[v], ac)
                resTD[v] = self.adjustment(accTD[v], v)
                ac = self.merge(ac, self.processing(resBU[v], v))
        return resTD
    
    def calc(self):
        self.topological_sort()
        accBU, resBU = self.bottom_up()
        resTD = self.top_down(resBU)

        res = [None] * self.V
        for v in self.order:
            res[v] = self.e if (v == self.order[0]) else self.processing(resTD[v], v)
            res[v] = self.merge(accBU[v], res[v])
            res[v] = self.adjustment(res[v], v)
        return res

#########################################################################################
N = int(input())
MOD = 10 ** 9 + 7
 
fact = [1] * (N + 1) # fact[n]: n!
factinv = [1] * (N + 1) # n!の逆元
for i in range(N):
    fact[i + 1] = fact[i] * (i + 1) % MOD
factinv[-1] = pow(fact[-1], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
    factinv[i] = factinv[i + 1] * (i + 1) % MOD
 
def main():
    RR = ReRooting(N, [1, 0])
    for _ in range(N - 1):
        a, b = map(int, input().split())
        RR.add_edge(a - 1, b- 1)
    print(*RR.solve(), sep="\n")
 
 
if __name__ == "__main__":
    main()