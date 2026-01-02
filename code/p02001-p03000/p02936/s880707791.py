#入力
n, q = map(int, input().split())
G = [[] for _ in range(n+1)]
for i in range(n-1):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

counter = [0 for _ in range(n+1)]
for _ in range(q):
    x, y = map(int, input().split())
    counter[x] += y

"""
#再帰
ans_dfs = [0 for _ in range(n)]
def dfs(now, parent, S):
    ans_dfs[now] = S + counter[now]
    for to in G[now]:
        if to == parent: continue
        dfs(to, now, ans_dfs[now])

"""
#非再帰
class p:
    num = -1
    parent = -1

    def __init__(self, x, y):
        self.num = x
        self.parent = y
#dfsでの探索順
node_list = []
ans = [0 for _ in range(n+1)]

def main():

    #dfs(1, -1, 0)
    #dfsでの探索順の作成
    stack = []
    stack.append(p(1, -1))
    while len(stack) != 0:
        now = stack.pop()
        node_list.append(now)
        for to in G[now.num]:
            if to == now.parent: continue
            stack.append(p(to, now.num))

    for now in node_list:
        ans[now.num] = counter[now.num] + ans[now.parent]

    for i in range(1, n+1): print(ans[i], end=' ')
    print()



if __name__ == '__main__':
    main()
