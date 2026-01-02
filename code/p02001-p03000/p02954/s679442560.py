import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

from math import log
def log2(x): return log(x, 2)


class Doubling(object):

    def __init__(self, N, K, next0):
        """
        ダブリングのメモ構築 O(NlogK)
        :param N: 解の存在空間の大きさ
        :param K: K個先までのステップを考慮する
        :param next0: i番目の要素の1個先の番号を要素として持つリスト
                      次の要素が存在しない場合には-1を要素として保持する
        """
        next = [[0] * N for _ in range(int(log2(K)) + 1)]
        next[0] = next0
        for k in range(int(log2(K))):
            for i in range(N):
                if next[k][i] == -1:
                    # 2^k個次に要素が無い時、当然2^(k+1)個次にも要素はない
                    next[k + 1][i] = -1
                else:
                    # i番目の要素の2^(k+1)個次の要素 := next[k][i](i番目の要素の2^k個次の要素)の2^k個先
                    next[k + 1][i] = next[k][next[k][i]]
        self.next = next

    def query(self, p, K):
        """
        p番目の要素のK個次の要素を求める O(logK)
        """
        for i in reversed(range(int(log2(K)) + 1)):
            if p == -1:
                return p
            if (K >> i) & 1:
                p = self.next[i][p]
        return p


S = input()

times = 2 * 10 ** 5
n0 = [i + 1 if c == 'R' else i - 1 for i, c in enumerate(S)]
d = Doubling(len(S), times, n0)

ans = [0] * len(S)
for i in range(len(S)):
    ans[d.query(i, times)] += 1
print(' '.join(str(x) for x in ans))
