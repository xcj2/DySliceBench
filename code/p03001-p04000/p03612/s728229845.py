import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    p = LI()
    ans = 0
    change = False

    for i,x in enumerate(p):
        num = i+1
        if num == x:
            if change:
                change = False
            else:
                change = True
                ans += 1
        else:
            change = False

    print(ans)
main()            
