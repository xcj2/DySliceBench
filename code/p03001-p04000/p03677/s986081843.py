class Binary_Indexed_Tree():
    def __init__(self, n):
        self.bit = [0]*n
        self.n = n
    def add(self, ind, num):
        while(ind <= self.n):
            self.bit[ind - 1] += num
            ind += ind & -ind
    def sum(self, ind):
        ret = 0
        while(ind > 0):
            ret += self.bit[ind-1]
            ind -= ind & -ind
        return ret

class Binary_Indexed_Tree_RAQ_RSQ():
    def __init__(self,n):
        self.p = Binary_Indexed_Tree(n+1)
        self.q = Binary_Indexed_Tree(n+1)

    def add(self, s,t,x):
        t += 1
        self.p.add(s,-x*s)
        self.p.add(t, x*t)
        self.q.add(s,x)
        self.q.add(t,-x)

    def sum(self, s, t):
        t += 1
        return self.p.sum(t) + self.q.sum(t)*t - self.p.sum(s) - self.q.sum(s)*s

n,m = map(int, input().split())
a = list(map(lambda x: int(x)-1, input().split()))
score = Binary_Indexed_Tree_RAQ_RSQ(2*m+10)


for i in range(n-1):
    cur, nxt = a[i], a[i+1]
    if cur > nxt:
        nxt += m
    if cur + 2 <= nxt:
        score.add(cur+3, nxt+1, 1)
        k = nxt-cur-1
        score.add(nxt+2, nxt+2, -k)

scores = [score.sum(0, i+1)+score.sum(0, i+m+1) for i in range(m)]

x = tmp = 0
for i in range(m):
    if scores[i] > tmp:
        x = i
        tmp = scores[i]
ans = 0

def cnt(cur, nxt):
    if cur > nxt:
        nxt += m
    return nxt-cur

for i in range(n-1):
    cur, nxt = a[i], a[i+1]
    ans += min(cnt(cur, nxt), cnt(x, nxt)+1)

print(ans)

