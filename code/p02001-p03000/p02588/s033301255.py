import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
A = []
for _ in range(N):
    a = LS2()
    if not '.' in a:
        a = int(''.join(a))
        a *= 10**9
        b,c = 0,0
        while a % 2 == 0:
            a //= 2
            b += 1
        while a % 5 == 0:
            a //= 5
            c += 1
        A.append((b-9,c-9))
    else:
        i = a.index('.')
        l = len(a)
        del a[i]
        a += ['0']*(9-l+1+i)
        a = int(''.join(a))
        b, c = 0, 0
        while a % 2 == 0:
            a //= 2
            b += 1
        while a % 5 == 0:
            a //= 5
            c += 1
        A.append((b - 9, c - 9))


from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1

ans = 0
for a in d.keys():
    b,c = a
    x = 0
    for e in d.keys():
        f,g = e
        if f >= -b and g >= -c:
            x += d[e]
    ans += d[a]*x

for a in d.keys():
    b,c = a
    if b >= 0 and c >= 0:
        ans -= d[a]

print(ans//2)
