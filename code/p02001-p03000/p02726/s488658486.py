import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, x, y = LI()
    ans = [0 for _ in range(n)]
    m = y-x-1

    for i in range(1,n):
        for j in range(i+1,n+1):
            direct = j-i
            short = abs(i-x) + 1 + abs(y-j)
            cnt = min(direct,short)
            ans[cnt] += 1

    print(*ans[1:],sep="\n")
main()
