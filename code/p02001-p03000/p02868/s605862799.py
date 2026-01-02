def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9)

    N, M = map(int, input().split())

    lst = [tuple(map(int, input().split())) for _ in range(M)]
    lst.sort(key = lambda x: x[1])
    lst.sort(key = lambda x: x[0])

    #セグメント木
    #次の2つの処理をO(log N)で実施することができる
    # s, tが与えられた時、区間[s, t)の最小値を求める
    # i, xが与えられた時、a_iの値をxに変更する

    INIT = 10 ** 18 #初期値 答えに関係ないもの
    MAX_N = 10 ** 6 #与えられる要素数の最大
    # INIT = 100
    data = [INIT] * (2 * MAX_N - 1) #MAX_Nで初期化

    #ここに機能をもたせる
    def func(vl, vr):
        return min(vl, vr)

    def init(n_):
        #簡単のため要素数を2のべき乗に
        n = 1
        while n < n_:
            n *= 2
        return n

    # N = int(input()) #配列の数
    n = init(N)

    def update(k, a): #k番目の値をaに変更 0-index
        # B[a] = k
        k += n - 1
        data[k] = a
        while k > 0: #登りながら更新
            k = (k - 1)//2
            data[k] = func(data[k * 2 + 1], data[k * 2 + 2])

    def query(a, b, k = 0, l = 0, r = n):
        if r <= a or b <= l:
            return INIT
        if a <= l and r <= b:
            return data[k]
        else:
            vl = query(a, b, k * 2 + 1, l, (l + r)//2)
            vr = query(a, b, k * 2 + 2, (l + r)//2, r)
            return func(vl, vr)

    def initialize(A): #リストAを与えて初期化する
        for i, a in enumerate(A):
            data[i + n - 1] = a
            # B[a] = i
        for i in range((2 * n - 3)//2, -1, -1):
            data[i] = func(data[i * 2 + 1], data[i * 2 + 2])

    # def index(a): #要素aがもとのどこに保存されているかを返す関数
    #     return B[a]

    def value(index): #indexが与えられた時、index番目の値を得る
        return data[index + n - 1]

    #初期値の入力
    D = [INIT] * N
    D[0] = 0
    # B = dict() #同じ要素がないのが前提 0-index管理
    initialize(D)

    #クエリの数
    # print (lst)
    # print (D)
    for a, b, c in lst:
        a -= 1
        b -= 1
        tmp = query(a, b)
        if D[b] > tmp + c:
            D[b] = tmp + c
            update(b, tmp + c)
        # print (D)

    # print (D)
    print (-1 if D[N - 1] == INIT else D[N - 1])

if __name__ == '__main__':
    main()