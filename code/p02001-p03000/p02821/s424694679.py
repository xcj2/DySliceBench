
INF = int(1e9)

def main():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    #Xより大きい要素の数を数える
    def counter(x):
        count = 0
        for i in range(n):
            l = -1
            r = n
            while r-l>1:
                mid = (l+r)//2
                if a[i] + a[mid] > x:
                    r = mid
                else:
                    l = mid
            count += n-r
        return count
    
    #Xより大きい要素数がm個未満であるXのうち最大のものを探す
    l = 0 
    r = INF
    while r-l>1:
        mid = (l+r)//2
        if counter(mid) < m:
            r = mid
        else:
            l = mid

    #lより大きい要素の総和を求める 
    def sigma(x):
        cnt = 0
        sgm = 0
        for i in range(n):
            l = -1
            r = n
            while r-l >1:
                mid = (l+r)//2
                if a[i]+a[mid]>x:
                    r = mid
                else:
                    l = mid
            cnt += n-r
            sgm += a[i] * (n-r) + (s[n]-s[r])
        return (sgm, cnt)

    sgm, cnt = sigma(l)
    ans = sgm+(m-cnt)*r
    print(ans)
main()