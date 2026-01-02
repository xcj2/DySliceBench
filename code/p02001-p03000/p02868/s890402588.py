import sys
input = sys.stdin.readline

class Segment_tree_Lazy:
    
    def __init__(self, n):
        
        self.init(n)
        
        #この次の処理は、求められる動作に応じて変化させる。ここでは区間最小問題のコードを書く。
        self.node = [self.inf]*self.size
        
        self.lazy = [self.inf]*self.size
        
        
    def init(self, n):
        
        self.inf = pow(2, 60)
        self.n = n
        
        self.N = 1
        while self.N < self.n:
            self.N *= 2
            
        self.size = self.N * 2 - 1
        self.N -= 1
        
        
    def evalate(self, k, l, r):
        
        if self.lazy[k] != self.inf:
            self.node[k] = min(self.lazy[k], self.node[k])
            
            if r-l > 1:
                if self.lazy[2*k+1] > self.lazy[k]:
                    self.lazy[2*k+1] = self.lazy[k]
                if self.lazy[2*k+2] > self.lazy[k]:
                    self.lazy[2*k+2] = self.lazy[k]
                
            self.lazy[k] = self.inf
         
            
    def update(self, a, b, x, k=0, l=0, r=-1):
        
        if r < 0:
            r = self.size - self.N
        
        if b <= l or r <= a:
            return 0
        
        if a <= l and r <= b:
            self.lazy[k] = x
            self.evalate(k, l, r)
            return 0
        
        self.update(a, b, x, 2*k+1, l, (l+r)//2)
        self.update(a, b, x, 2*k+2, (l+r)//2, r)
        self.node[k] = min(self.node[2*k+1], self.node[2*k+2])
        
        
    def find(self, a, b, k, l, r):
        
        if r <= a or b <= l:
            return self.inf
        
        self.evalate(k, l, r)
        
        if a <= l and r <= b:
            return self.node[k]
        
        find_l = self.find(a, b, 2*k+1, l, (l+r)//2)
        find_r = self.find(a, b, 2*k+2, (l+r)//2, r)
        return min(find_l, find_r)
    
    
    def count(self, l, r):
        
        return self.find(l, r, 0, 0, self.size-self.N)
    
    
    
    

def main():
    n, m = map(int, input().split())
    
    inf = pow(2, 60)
    dp = [inf]*(n)
    dp[0] = 0
    
    node = [[] for _ in range(n)]
    segment = Segment_tree_Lazy(n)
    
    segment.update(0, 1, 0)
    for i in range(m):
        s, t, c = map(int, input().split())
        node[t-1].append((s-1, c))
        segment.update(s, t, c)
    
    for i in range(n-1):
        dp[i+1] = dp[i] + min(segment.node[segment.N+i+1], segment.lazy[segment.N+i+1])
        for (v, c) in node[i+1]:
            dp[i+1] = min(dp[i+1], dp[v]+c)
        index = i
        while True:
            if dp[index] > dp[index+1]:
                dp[index] = dp[index+1]
                index -= 1
            else:
                break
    
    print(dp[n-1] if dp[n-1] < inf else -1)
    
    
if __name__ == "__main__":
    main()
