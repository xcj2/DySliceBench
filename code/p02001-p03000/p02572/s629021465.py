from sys import stdin, stdout
def gmi(): return map(int, stdin.readline().strip().split())
def gms(): return map(str, stdin.readline().strip().split())
def gari(): return list(map(int, stdin.readline().strip().split()))
def gars(): return list(map(int, stdin.readline().strip().split()))
def gs(): return stdin.readline().strip()
def gls(): return list(stdin.readline())
def gi(): return int(stdin.readline())

n = gi()
ar = gari()
c = 0
ans = 0
s = sum(ar)
sub = 0
for i in ar[:-1]:
    sub +=  ar[c]
    ans += i*(s-sub)
    c += 1
print(ans%1000000007)






