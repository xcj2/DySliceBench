import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

n,m,s=l_in()

uvab=[]
edges = [[] for _ in range(n)]
for _ in range(m):
    u,v,a,b = l_in()
    edges[u-1].append((v-1,a,b))
    edges[v-1].append((u-1,a,b))

cd = [l_in() for _ in range(n)]

# dp[i][g] city i で g まいの銀貨をもつための最小時間
m = 50*n+1
#m = 4
dp = [[-1]*m for _ in range(n)]


from heapq import heappush,heappop
h = []

for g in range(min(s+1,m+3)):
    heappush(h, (0,-g,0))

while len(h) > 0:
    t,g,i = h[0]
    g = -g
#    print("t,g,i", t,g,i)
    #

    heappop(h)
    if dp[i][min(g,m-1)] != -1:
        continue

    
    dp[i][min(g,m-1)] = t
    
    for v,a,b in edges[i]:
        if g-a >= 0 and dp[v][min(g-a,m-1)] == -1:
            heappush(h,(t+b,-(g-a),v))
#            print("push", t+b,-g+a,v)

    c,d = cd[i]
    heappush(h,(t+d,-(g+c),i))
    
#    if dp[i][min(g+c,m-1)] == -1:

for d in dp:
    pass
#    print(d)


for i in range(1, n):
    res = -1
    for v,a,b in edges[i]:
        min_t = -1
        for g in range(a,m):
            t = dp[v][g]
            if t == -1:
                continue
            if min_t == -1 or min_t > t:
                min_t = t
#                print("min_t", v,g,min_t)

        if res == -1 or res > min_t+b:
            res = min_t+b

#    print(dp[i])
    for t in dp[i]:
        if t == -1:
            continue
        if res == -1  or t < res:
            continue
            res = t
            
    print(res)
        
