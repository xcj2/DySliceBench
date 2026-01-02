def factorial(n):
    'n!を返す関数'
    ans = 1
    while(n > 0):
        ans *= n
        n -= 1
    return ans

def nCr(n, r):
    '''
    nCrを返す関数
    階乗を返すfactorial()関数に依存している
    組み合わせの値は必ず整数値になるのでintとしてreturnしている
    '''
    ans = factorial(n) / (factorial(r) * factorial(n-r))
    return int(ans)

class UnionFind:
    def __init__(self, N):
        '''
        親の番号を格納する。親だった場合は-(その集合のサイズ)とする。
        作る時はparentの値を全て-1にすることで、全てバラバラになる。
        '''
        self.N = N
        self.parent = [-1 for i in range(self.N)]

    def root(self, A):
        'Aがどのグループに属しているか調べる。'
        if self.parent[A] < 0:
            return A
        else:
            self.parent[A] = self.root(self.parent[A])
            return self.parent[A]

    def size(self, A):
        '自分のいるグループの頂点数を調べる。'
        return -self.parent[self.root(A)]

    def connect(self, A, B):
        '''
        AとBをくっつける。
        AとBを直接繋ぐのではなく、root(A)にroot(B)をくっつける。
        '''
        A = self.root(A)
        B = self.root(B)
        if A == B:
            # すでにくっついているからくっつけない。
            return False
        elif self.size(A) < self.size(B):
            # 大小が逆だったらひっくり返す。
            A, B = B, A
        else:
            pass
        # Aのサイズを変更する。
        self.parent[A] += self.parent[B]
        # Bの親をAに変更する。
        self.parent[B] = A
        return True

islands, bridges = map(int, input().split())
A, B = [], []
ans = [0 for i in range(bridges)]
# ans[bridges-1] = nCr(islands, 2)
ans[bridges-1] = int(islands * (islands-1) / 2)

UF = UnionFind(islands)

for i in range(bridges):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

for i in range(bridges-1, 0, -1):
    if UF.root(A[i]) != UF.root(B[i]):
        ans[i-1] = ans[i] - UF.size(A[i]) * UF.size(B[i])
        UF.connect(A[i], B[i])
    else:
        ans[i-1] = ans[i]

for i in range(bridges):
    print(ans[i])
