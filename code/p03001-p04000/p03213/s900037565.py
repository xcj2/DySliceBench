def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

n = getN()
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

yaku = []
for i in range(2,n+1):
    yaku = yaku + (primes(i))


from collections import defaultdict
yakunum = defaultdict(int)
for i in yaku:
    yakunum[i] += 1


over2, over4, over14, over24, over74 = 0,0,0,0,0
for i in yakunum.values():

    if i > 1:
        over2 += 1
    if i > 3:
        over4 += 1
    if i > 13:
        over14 += 1
    if i > 23:
        over24 += 1
    if i > 73:
        over74 += 1

#print(over2, over4, over14, over24, over74 )
ans = over74 + (over24*over2)-(over24) + (over14*over4)-over14 + ((over4)*(over4-1)*(over2-2))//2

print(ans)