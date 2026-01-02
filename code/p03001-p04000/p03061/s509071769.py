#0WA n==1 mod saikikilimit exit
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))


#a,bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#リスト l の最大公約数
def gcdlist(l):
    a = l[0]
    for i in range(len(l)):
        a = gcd(a,l[i])
    return a

#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass #sortされていない

#0番目ぶー
res = gcdlist(a[1::])

#else
p = sorted(divisor(a[0]))
for i in range(len(p)-1,-1,-1):
    if p[i]<=res:
        break
    cnt = 1
    for j in range(1,n):
        if a[j]%p[i]==0:
            cnt += 1
    if cnt >= n-1:
        res = p[i]
        break
print(res)