import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

# パスを計算
h,w,d = li()
grid = []
dic = {}
for i in range(h):
    row = list(li())
    for j in range(w):
        dic.update({row[j]: (i,j)})

dist = [0]*(h*w+1)

for i in range(d+1,h*w+1):
    dist[i] = dist[i-d] + abs(dic[i][0] - dic[i-d][0]) + abs(dic[i][1] - dic[i-d][1])
    
q = ni()
for _ in range(q):
    l,r = li()
    print(dist[r] - dist[l])