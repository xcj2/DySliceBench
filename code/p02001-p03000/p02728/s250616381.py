#import sys
#input = lambda: sys.stdin.readline().rstrip()

#MOD
P = 10**9 + 7
N = 200001 #使う最大値+1以上にする、値に注意3*10^5とかにしとくと安心
inv = [0] + [1] # 1/x
finv = [1] + [1] # 1/x!
fac = [1] + [1] # x!
for i in range(2, N):
  inv += [inv[P % i] * (P - int(P / i)) % P]
  fac += [(fac[i-1] * i) % P]
  finv += [(finv[i-1] * inv[i]) % P]

def comb(a, b): return (fac[a] * ((finv[b] * finv[a-b]) % P)) %P

#全方位木dp
#-------------------------------------------------------------------
#扱うクラス
class T:
    num = 1
    child = 0

    def __init__(self, a, b):
        self.num = a
        self.child = b

#零元
zero = T(1, 0)
#一個上に遷移した時の変化
def step(x):
    return T(x.num, x.child+1)
#マージ
def merge(x, y):
    return T((x.num*y.num*comb(x.child+y.child, x.child))%P, x.child+y.child)

G = [[] for _ in range(N)]
down_data = [zero for _ in range(N)]
dat = [zero for _ in range(N)]
rev_data = [zero for _ in range(N)]

class p:
    num = -1
    parent = -1

    def __init__(self, x, y):
        self.num = x
        self.parent = y
node_list = []
def makeNodeList(root):
    #dfsでの探索順の作成
    stack = []
    stack.append(p(root, -1))
    while len(stack) != 0:
        now = stack.pop()
        node_list.append(now)
        for to in G[now.num]:
            if to == now.parent: continue
            stack.append(p(to, now.num))
    node_list.reverse()

def dfs(root):
    for now in node_list:
        for to in G[now.num]:
            if to == now.parent: continue
            down_data[now.num] = merge(down_data[now.num], step(down_data[to]))

def dfs_rev(root):
    for now in node_list:
        #累積
        rev = rev_data[now.num]
        left = []
        right = []
        cnt = 0
        for to in G[now.num]:
            if to==now.parent: continue
            if len(left)==0: left.append(step(down_data[to]))
            else: left.append(merge(left[cnt-1], step(down_data[to])))
            cnt += 1
        cnt = 0
        for to in reversed(G[now.num]):
            if to==now.parent: continue
            if len(right)==0: right.append(step(down_data[to]))
            else: right.append(merge(right[cnt-1], step(down_data[to])))
            cnt += 1
        dat[now.num] = merge(rev, down_data[now.num])
        cnt = 0
        for to in G[now.num]:
            if to==now.parent: continue
            x = zero if cnt==0 else left[cnt-1]
            y = zero if cnt==len(right)-1 else right[len(right)-2-cnt]
            rev_data[to] = step(merge(rev, merge(x, y)))
            cnt += 1

def calc(data_num):
    root = -1
    for i in range(1, data_num+1):
        if len(G[i]) == 1:
            root = i
            break
    makeNodeList(root)
    dfs(root)
    node_list.reverse()
    dfs_rev(root)
#-------------------------------------------------------------------
def main():
    n = int(input())
    for i in range(n-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    calc(n)

    for i in range(1, n+1): print(dat[i].num)

if __name__ == "__main__": main()
