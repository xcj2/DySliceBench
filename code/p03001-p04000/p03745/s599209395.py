import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    tp = 0
    ans = 1
    
    for i in range(1,n):
        before = a[i-1]
        after = a[i]

        if tp == 0:
            if before < after:
                tp = 1
            elif before > after:
                tp = -1
        elif tp == 1:
            if before > after:
                ans += 1
                tp = 0
        elif tp == -1:
            if before < after:
                ans += 1
                tp = 0
        
    print(ans)



main()            
