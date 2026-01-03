import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    lst = [None for _ in range(n)]

    for i in range(n-1,-1,-1):
        a,b = LI()
        lst[i] = [a,b]
    cumsum = 0
    for a,b in lst:
        a += cumsum
        add = (b-(a%b))%b
        cumsum += add

    ans = cumsum
    print(ans)
main()            
