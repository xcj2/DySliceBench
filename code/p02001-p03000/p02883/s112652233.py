def check(res,a,f,k):
    for sa,sf in zip(a,f):
        if sa*sf <= res:
            continue
        k -= sa - (res // sf)
        if k < 0:
            return False
    return True


def nibun(l,r,a,f,k):
    if r == l:
        return l
    flag = (l+r)//2
    if check(flag,a,f,k):
        return nibun(l,flag,a,f,k)
    else:
        return nibun(flag+1,r,a,f,k)

def main():
    n,k = map(int,input().split())
    a= list(map(int,input().split()))
    f= list(map(int,input().split()))

    a.sort()
    f.sort(reverse=True)

    return nibun(0,10**13,a,f,k)


print(main())