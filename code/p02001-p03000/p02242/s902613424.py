class Graph:
    def __init__(self,V,E):
        self.V = V
        self.E = E

    def WF(self,st):
        N,INF = len(self.V),10**7+1
        dp = [INF for _ in range(N)]
        #dp[i]:頂点stから頂点iへの最小距離
        dp[st] = 0
        update = True
        while update:
            update = False
            for i in range(N):
                for j in range(N):
                    if (j,i) in self.E:
                        if dp[i] > dp[j] + self.E[(j,i)]:
                            dp[i] = dp[j] + self.E[(j,i)]
                            update = True
        return dp

def main():
    n = int(input())
    I = [list(map(int,input().split())) for _ in range(n)]
    V = set([i for i in range(n)])
    E = {}
    for i in range(n):
        for j in range(I[i][1]):
            E[(I[i][0],I[i][j*2+2])] = I[i][j*2+3]
    G = Graph(V,E)
    sp = G.WF(0)
    for i in range(n):
        print(i,sp[i])

if __name__ == "__main__":
    main()

