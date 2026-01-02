import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    height = LI()
    ans = 0
    cnt = 0
    mn = height[0]

    for h in height[1:]:
        if mn>=h:
            cnt += 1
            mn = h
            ans = max(ans, cnt)
        else:
            cnt = 0
            mn = h

    print(ans)
main()
