import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    n, k= LI()
    x = LI()
    ans = float("inf")

    for i in range(n-k+1):
        if x[i] >= 0 or x[i+k-1] <= 0:
            time = max(abs(x[i]), abs(x[i+k-1]))
            ans = min(ans, time)
        else:
            time = min(abs(x[i]), abs(x[i+k-1]))*2 + max(abs(x[i]), abs(x[i+k-1]))
            ans = min(ans, time)

    print(ans)

main()



