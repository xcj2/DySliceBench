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
    # 最大は, (n-1)+m 
    # kn >= (n-1)+m
    # k >= 1 +(m-1)/n
    k = 1 - (-(m-1)//n)
    si = s*k
    a = KMP(t)
    b = a.match(si)
    edges = [[] for i in range(n)]
    for i in range(n):
        if b[i]:
            edges[i].append((i+m)%n)
    # loopを見つける
    # start地点をすべて試す
    # 進む方向、戻る方向について別々に求める
    visited = [0]*n
    loop = False
    ans = 0
    for i in range(n):
        # 他のパスから辿られている場合
        if visited[i]:
            continue
        visited[i] = 1
        # →に進む
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
    print(ans)

if __name__ == "__main__":
    main()