import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, k = LI()
    a = LI()
    ans = 0
    num = 10**9 + 7

    for i in range(n):
        x = a[i]
        before = 0
        after = 0

        for j in range(i):
            if a[j] < x:
                before += 1

        for j in range(i+1, n):
            if a[j] < x:
                after += 1


        ans += (after*(k+1)+before*(k-1))*k // 2
        ans %= num

    ans = print(ans)
main()
