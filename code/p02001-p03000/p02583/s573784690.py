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
L = LI()

ans = 0
for i in range(N-2):
    a = L[i]
    for j in range(i+1,N-1):
        b = L[j]
        for k in range(j+1,N):
            c = L[k]
            if a == b or b == c or c == a:
                continue
            else:
                if a+b > c and b+c > a and c+a > b:
                    ans += 1
print(ans)
