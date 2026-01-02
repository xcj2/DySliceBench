h,w,k=map(int,input().split())
def amida_h1_total(w):
    if w<0:
        return 0
    if w==0:
        return 1
    return amida_h1_total(w-1)+amida_h1_total(w-2)
def amida(h,w,k):
    memo=[[-1 for _ in range(w)] for _ in range(h)]
    memo[0][0]=amida_h1_total(w-1)
    if w>1:
        memo[0][1]=amida_h1_total(w-2)
    for i in range(2,w):
        memo[0][i]=0
    def _amida(h,k):
        if k<=0 or k>w:
            return 0
        if memo[h-1][k-1]>=0:
            return memo[h-1][k-1]
        memo[h-1][k-1]=sum((_amida(h-1,k-1)*amida_h1_total(k-2)*amida_h1_total(w-k),
                            _amida(h-1,k)  *amida_h1_total(k-1)*amida_h1_total(w-k),
                            _amida(h-1,k+1)*amida_h1_total(k-1)*amida_h1_total(w-k-1)))%1000000007
        return memo[h-1][k-1]
    return _amida(h,k)
print(amida(h,w,k))
