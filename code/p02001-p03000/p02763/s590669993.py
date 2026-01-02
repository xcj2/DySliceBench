class BIT:
    """
    https://tjkendev.github.io/procon-library/python/range_query/bit.html
    Binary index treeの実装
    配列[a1, a2,...,an]に対して以下のクエリをO(logn)で行う:
        1. aiにxを加える
        2. 区間和 ai + a(i+1) + ... + aj の和を求める
    """
    def __init__(self, n):
        """
        添字は1スタート
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def add(self, i, x):
        """
        i>0に対してaiにxを加算(x < 0でもOK)
        """
        if i <= 0 or self.n < i:
            print("i should be within 1 to n")
        else:
            self.el[i] += x
            while i <= self.n:
                self.data[i] += x
                i += i & -i

    def sum(self, i):
        """
        添字1からiまでの累積和を求める
        """
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def get(self, i, j=None):
        """
        添字iからjまでの累積和を求める
        j=Noneの場合はaiの値を返す
        """
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i - 1)


"""
ここから本問の解答
各アルファベットごとにBITを作成する
"""

N = int(input())
S = list(input())
Q = int(input())

# ここを Alphabet = [BIT(N)] * 26とすると、
# どうもすべてのAlphabet[i]が連動するらしい
Alphabet = [None] * 26
for i in range(26):
    Alphabet[i] = BIT(N)

# Sの初期値からBITを初期化
for i, s in enumerate(S):
    num = ord(s) - 97
    Alphabet[num].add(i + 1, 1)

"""
各クエリごとに行う操作を関数にまとめておく
"""
def change(i, c):
    if S[i - 1] != c:
        pre = ord(S[i - 1]) - 97
        Alphabet[pre].add(i, -1)
        post = ord(c) - 97
        Alphabet[post].add(i, 1)
        S[i - 1] = c

def appear(l, r):
    char = 0
    for i in range(26):
        if Alphabet[i].get(l, r) >= 1:
            char += 1
    return char

"""
クエリ処理
"""

for _ in range(Q):
    flag, x, y = input().split()
    if flag == "1":
        i, c = int(x), y
        change(i, c)
    elif flag == "2":
        l, r = int(x), int(y)
        print(appear(l, r))
