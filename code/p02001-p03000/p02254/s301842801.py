import sys, collections, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    S = SS()

    # ハフマン木の構成
    cnt = collections.Counter(S)
    # (頻度, 文字, 左の子, 右の子)
    freq = [(v, k, None, None) for k, v in cnt.items()]
    heapq.heapify(freq)
    while len(freq) >= 2:
        l = heapq.heappop(freq)
        r = heapq.heappop(freq)
        heapq.heappush(freq, (l[0]+r[0], '', l, r))
    root = heapq.heappop(freq)

    # 符号長の導出
    code_len = {}
    for i in cnt.keys():
        code_len[i] = 1

    def dfs(node, depth):
        if node[1]:
            if depth == 0:
                code_len[node[1]] = 1
            else:
                code_len[node[1]] = depth
        else:
            dfs(node[2], depth+1)
            dfs(node[3], depth+1)

    dfs(root, 0)

    # 符号の長さの計算
    # print(code_len)
    ans = 0
    for i in S:
        ans += code_len[i]
    print(ans)

if __name__ == '__main__':
    resolve()

