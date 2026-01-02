import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m = LI()
    span = [None for _ in range(m)]
    for i in range(m):
        a, b = LI()
        span[i] = [a,b]
    span.sort(key=lambda x: x[1])
    choice = [0, 0]
    ans = 0
    for each_span in span:
        if choice[1]<=each_span[0]:
            choice = each_span
            ans += 1
    print(ans)
main()
