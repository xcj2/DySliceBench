import sys
sys.setrecursionlimit(100000)

def ii(): return int(input())
def iis(): return input().split()
def imi(): return map(int,iis())
def iil(): return list(imi())


factmemo={0:1} #階乗
def fact(n):
    if n in factmemo:
        return factmemo[n]
    k = n*fact(n-1)
    factmemo[n]=k
    return k

def comb(a,b):
    if a-b < 0:
        return 0
    return fact(a)//(fact(a-b)*fact(b)) #組み合わせ

def aaa(n,k):
    r = len(str(n))-1
    st = str(n)
    ans = 0
    if k==1 and r>=0:
        ans += 9*r \
               + int(st[0])
    elif k==2 and r>=1:
        ans += 9**2 * comb(r, 2) \
               + (int(st[0])-1) * 9**1 * comb(r, 1) \
               + aaa(n%(10**r), k-1)
    elif k==3 and r>=2:
        ans += comb(r, 3)*9**3\
               +comb(r, 2)*9**2*(int(st[0])-1)\
               +aaa(n%(10**r), k-1)
    return ans

n = int(input())
k = int(input())
ans = aaa(n,k)
print(ans)