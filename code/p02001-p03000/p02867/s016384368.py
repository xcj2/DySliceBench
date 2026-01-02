def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = sorted([[a[i], b[i]] for i in range(n)], key=lambda x: x[1])

    base=[a for a,b in ab]
    #ini：上限（下限）,base：元の配列,monoid：モノイド,tree：セグ木,depth：treeの深さ,
    #basesize：baseの要素数,treesize：treeの要素数,num：treesize-basesize
    # 初期値（上限とか下限）を決定
    ini=10**9+1
    #セグ木の要素数（num）および深さ（depth）を計算
    basesize=len(base)
    num,depth=1,1
    while num<basesize:
        num*=2
        depth+=1
    num-=1
    #関数（モノイド、今回はmin）を設定
    monoid=min
    #セグ木を構築
    treesize=num*2+1
    tree=[None]*treesize
    #segtree[m]以降に代入したい配列を入力していく
    for i in range(num,num+basesize):tree[i]=base[i-num]
    for i in range(num+basesize, treesize):tree[i]=ini
    #segtree[m]以降の情報を使って、0に向かってセグ木を構築していく
    for i in range(num-1,-1,-1):
        tree[i]=monoid(tree[2*i+1],tree[2*i+2])
    
    #条件を満たす(サンプルの条件はs以下になること)最大のインデックスを返す関数
    def max_index(index_func):
        #探していく
        i=0
        while i<num:
            k=2*i+1
            if index_func(tree[k+1]):
                i=k+1
                continue
            if index_func(tree[k]):
                i=k
                continue
            return -1
        return i-num

    #条件を満たす(サンプルの条件はs以下になること)最小のインデックスを返す関数
    def min_index(index_func):
        #探していく
        i=0
        while i<num:
            k=2*i+1
            if index_func(tree[k]):
                i=k
                continue
            if index_func(tree[k+1]):
                i=k+1
                continue
            return -1
        return i-num

    #半開区間[lower,upper)の最小値（とか）を探す関数
    def search(lower,upper):
        #返り値を初期化
        ret=ini
        l=lower+num
        r=upper+num
        while l<r:
            if r%2==0:
                r-=1
                ret=monoid(ret,tree[r])
            if l%2==0:
                ret=monoid(ret,tree[l])
                l+=1
            l//=2
            r//=2
        return ret

    #base[i]をsに更新したときにセグ木全体を更新する関数
    def update(index,new_value):
        i=index+num
        tree[i]=new_value
        while i!=0:
            i=(i-1)//2
            temp=monoid(tree[2*i+1],tree[2*i+2])
            if tree[i]!=temp:
                tree[i]=temp
                continue
            break
    
    cnt = 0
    for i in range(n):
        a,b=ab[i][0],ab[i][1]
        if a > b:
            t = max_index(lambda x:x<=b)
            if t <= i:
                print("No")
                return 0
            update(i, a)
            update(t, a)
            ab[i][0], ab[t][0] = ab[t][0], a
            cnt+=1
    if cnt <= n - 2:
        print("Yes")
    else:
        print("No")
main()