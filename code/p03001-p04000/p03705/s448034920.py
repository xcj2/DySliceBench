import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,a,b = LI()
    ans = 0
    if n == 1:
        if a == b:
            ans = 1
        else:
            ans = 0
    elif n == 2:
        if a <= b:
            ans = 1
        else:
            ans = 0
    else:
        if a <= b:
            summin = a*(n-1) + b
            summax = a + b*(n-1)
            ans = summax - summin + 1
        else:
            ans = 0

    print(ans)
        
main()            
