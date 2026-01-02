
A,B = map(int,input().split())

#素数列挙
def searchPrimeNum(N):
    max = int(N**0.5)
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum



#素因数分解(素数列挙が必要)
def pfact(N):
    plis = searchPrimeNum(int(N**0.5+1))
    ans = 1
    for p in plis:
        if N%p == 0:
            ans += 1
            N = N//p
        while N%p == 0:
            N = N//p
        if N == 1:
            break
    if N != 1:
        ans += 1
    return ans

#互除法(最大公約数)
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(pfact(gcd(A,B)))