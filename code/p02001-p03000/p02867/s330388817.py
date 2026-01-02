def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = sorted([[a[i], b[i]] for i in range(n)], key=lambda x: x[1])

    num=1
    while num < n:
        num *= 2
    num-=1
    inf=10**9+1

    m=num+n
    segtree=[inf]*m
    for i in range(num,m):
        segtree[i] = ab[i - num][0]
    for i in range(num-1,-1,-1):
        j=2*i+1
        if j>=m:
            segtree[i]=inf
        elif j+1>=m:
            segtree[i]=segtree[j]
        else:
            segtree[i] = min(segtree[j], segtree[j + 1])

    #探す
    def search(s):
        i=0
        while i < num:
            k = 2 * i + 1
            if k+2<=m:
                if segtree[k+1] <= s:
                    i = k + 1
                    continue
            if k+1<=m:
                if segtree[k] <= s:
                    i = k
                    continue
            return - 1
        return i - num
    
    #更新
    #def update_good(i, s):
    #    while True:
    #        if segtree[i] > s:
    #            segtree[i] = s
    #            i = (i - 1) // 2
    #            continue
    #        break
    
    def update(i, s):
        segtree[i]=s
        while i!=0:
            k=(i - 1) // 2
            if i % 2 == 1:
                temp = min(segtree[min(i + 1, m - 1)], segtree[i])
            else:
                temp = min(segtree[i-1],segtree[i])
            if segtree[k]!=temp:
                segtree[k] = temp
                i = k
                continue
            break

    cnt = 0
    for i in range(n):
        a,b=ab[i][0],ab[i][1]
        if a > b:
            t = search(b)
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