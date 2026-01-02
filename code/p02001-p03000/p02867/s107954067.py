def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = sorted([[a[i], b[i]] for i in range(n)], key=lambda x: x[1])

    #セグ木の要素数（num）および階層（fl）を計算
    num = 1
    fl = 1
    while num < n:
        num *= 2
        fl+=1
    num -= 1

    #上限（inf）を決定(下限とかに適宜変える)
    inf = 10 ** 9 + 1

    #関数（モノイド、今回はmin）を設定
    monoid=min

    #セグ木を構築
    m=num+n
    segtree = [None] * m
    #segtree[m]以降に代入したい配列を入力していく
    for i in range(num, m):
        segtree[i] = ab[i - num][0]
    #segtree[m]以降の情報を使って、0に向かってセグ木を構築していく
    for i in range(num - 1, -1, -1):
        j=2*i+1
        if j>=m:
            segtree[i]=inf
        else:
            segtree[i] = monoid(segtree[j], segtree[min(j + 1, m - 1)])

    #条件を満たす(サンプルの条件はs以下になること)最大のインデックスを返す関数
    def max_index(s):
        #条件の定義
        func = lambda x: x <= s
        #探していく
        i=0
        while i < num:
            k = 2 * i + 1
            if k + 1 < m:
                if func(segtree[k + 1]):
                    i = k + 1
                    continue
            if k < m:
                if func(segtree[k]):
                    i = k
                    continue
            return - 1
        return i - num
            
    #半開区間[lower,upper)の最小値（とか）を探す関数
    def search_new(lower, upper):
        q = [[0, 1]]  #インデックス、階層
        #返り値を初期化
        ret = inf      
        while q:
            i, f = q.pop()
            #popしたインデックスと階層から、求める下限と上限を算出する
            #幅
            width = pow(2, fl - f)
            #下限と中央と上限
            kagen = (i - pow(2, f - 1) + 1) * width
            chuo = kagen + width // 2
            jogen = kagen + width
            k = 2 * i + 1
            if lower <= kagen and jogen <= upper:
                ret = monoid(ret, segtree[i])
                continue
            if k < m:
                if lower <= kagen and chuo <= upper:
                    ret = monoid(ret, segtree[k])
                elif lower <= chuo:
                    q.append([k, f + 1])
            if k + 1 < m:
                if lower <= chuo and jogen <= upper:
                    ret = monoid(ret, segtree[k + 1])
                elif chuo <= upper:
                    q.append([k + 1, f + 1])
        return ret

    #segtree[i]をsに更新したときにセグ木全体を更新する関数
    def update(i, s):
        segtree[i] = s
        temp = s
        while i!=0:
            k = (i - 1) // 2
            if i % 2 == 1:
                temp = monoid(segtree[min(i + 1, m - 1)], temp)
            else:
                temp = monoid(segtree[i - 1], temp)
            if segtree[k]!=temp:
                segtree[k] = temp
                i = k
                continue
            break

    cnt = 0
    for i in range(n):
        a,b=ab[i][0],ab[i][1]
        if a > b:
            t = max_index(b)
            if t <= i:
                print("No")
                return 0
            update(num + i, a)
            update(num + t, a)
            ab[i][0], ab[t][0] = ab[t][0], a
            cnt+=1
    if cnt <= n - 2:
        print("Yes")
    else:
        print("No")
    
main()