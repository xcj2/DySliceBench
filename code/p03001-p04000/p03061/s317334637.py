# @profile
def main():
    import math

    N=int(input())
    a = list(map(int,input().split()))

    # N=5
    # a = [12,15,18,36,42]

    # N = 10**5
    # a = [1]*N

    # N=11
    # a = [56,58,82,46,67,36,98,68,24,46,52]

    #a,bの最大公約数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 一番近い大きい側の2の累乗の数が，segtreeの葉の数になる．
    N_ADJUST = 2**int(math.ceil(math.log(N)/math.log(2)))
    # segtreeのサイズはN_ADJUSTを葉とする木のノード数．
    ST_SIZE = N_ADJUST*2-1
    # binopに合わせて単位元として決める．maxならINT_MAX(問題文の制限)
    INT_IDENTITY = 0
    li = [INT_IDENTITY]*ST_SIZE
    # li_initは，葉の配列．
    # 節点kが [l,r) にbinopという演算で結びついている．
    def init_segtree(li, k, l, r, binop, li_init):
        if r-l==1:
            li[k] = INT_IDENTITY if l >= len(li_init) else li_init[l]
        elif r-l>1:
            k_l, k_r = k*2+1, k*2+2
            init_segtree(li, k_l, l, (l+r)//2, binop, li_init)
            init_segtree(li, k_r, (l+r)//2, r, binop, li_init)
            li[k] = binop(li[k_l],li[k_r])

    init_segtree(li,0,0,N_ADJUST,gcd,a)

    # print(li)
    # 下からupdateする．
    def update_segtree(li,k,binop):
        if k > 0:
            k_2 = (k-1)//2
            k_l = k_2*2+1
            k_r = k_l+1
            li[k_2] = binop(li[k_l],li[k_r])
            update_segtree(li,k_2,binop)

    val = []
    for i in range(N_ADJUST-1,N_ADJUST+N-1):
        tmp = li[i]
        li[i] = 0
        update_segtree(li,i,gcd)
        # print(i, li)
        val.append(li[0])
        li[i] = tmp
        update_segtree(li,i,gcd)

    print(max(val))

main()
