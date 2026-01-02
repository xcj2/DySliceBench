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
#    edges = [[] for i in range(n)]
#    for i in range(n):
#        if b[i]:
#            edges[i].append((i+m)%n)
#    
#    def dfs(node):
#        if visited[node] == 1:
#            return True
#        if visited[node] == 2:
#            return False
#        visited[node] = 1
#        for nei in edges[node]:
#            if dfs(nei):
#                return True
#        visited[node] = 2
#        res.append(node)
#        return False
#    visited = [-1] * n
#    res = []
#    for i in range(n):
#        if dfs(i):
#            return -1
#    dp = [0] * n
#    ans = 0
#    for i in range(n-1, -1, -1):
#        t = res[i]
#        for c in edges[t]:
#            dp[c] = max(dp[c], dp[t] + 1)
#            ans = max(ans, dp[c])
#    return ans

            
    visited = [0]*n
    loop = False
    ans = 0
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        cur = i
        right = 0
        while b[cur]:
            nxt = (cur + m) % n
            if visited[nxt]:
                loop = True
                break
            visited[nxt] = 1
            cur = nxt
            right += 1
        cur = i
        left = 0
        while b[(cur-m)%n]:
            nxt = (cur-m) % n
            if visited[nxt]:
                loop = True
                break
            visited[nxt] = 1
            cur = nxt
            left += 1
        if not loop:
            ans = max(ans, right+left)
        else:
            ans = -1
            break
    return ans

if __name__ == "__main__":
    print(main())