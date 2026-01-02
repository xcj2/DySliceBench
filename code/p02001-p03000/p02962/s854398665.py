import collections
class KMP():
    def __init__(self, pattern):
        self.pattern = pattern
        self.n = len(pattern)
        self.create_k_table()
    
    def create_k_table(self):
        ktable = [-1]*(self.n+1)
        j = -1
        for i in range(self.n):
            while j >= 0 and self.pattern[i] != self.pattern[j]:
                j = ktable[j]
            j += 1
            if i+1 < self.n and self.pattern[i+1] == self.pattern[j]:
                ktable[i+1] = ktable[j]
            else:
                ktable[i+1] = j
        self.ktable = ktable

    def match(self,s):
        n = len(s)
        j = 0
        ret = [0]*n
        for i in range(n):
            while j >= 0 and (j == self.n or s[i] != self.pattern[j]):
                j = self.ktable[j]
            j += 1
            if j == self.n:
                ret[(i-self.n+1)%n] = 1 
        return ret

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    k = 1 - (-(m-1)//n)
    si = s*k
    a = KMP(t)
    b = a.match(si)
    edges = [[] for i in range(n)]
    indegree = [0] * n
    for i in range(n):
        k = (i+m)%n
        if b[i]:
            edges[i].append(k)
            indegree[k] += 1
    
    def topSort():
        q = collections.deque([i for i in range(n) if indegree[i] == 0])
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in edges[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return len(res) == n
    
    res = []
    dp = [0] * n
    flag = topSort()
    if flag:
        for k in range(n):
            i = res[k]
            for j in edges[i]:
                dp[j] = max(dp[j], dp[i] + 1)
        ans = max(dp)
    else:
        ans = -1
    return ans
     

if __name__ == "__main__":
    print(main())
