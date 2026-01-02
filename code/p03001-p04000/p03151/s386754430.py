import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    b = LI()
    need = 0
    ans = 0
    surplus = []
    for i in range(n):
        if a[i]>=b[i]:
            surplus.append(a[i]-b[i])
        else:
            need += b[i] - a[i]
            ans += 1
    
    surplus.sort(reverse=True)

    if need <= 0:
        print(0)
        exit(0)
    else:
        for r in surplus:
            need -= r
            ans += 1
            if need <= 0:
                print(ans)
                exit(0)
        
        print(-1)
main()
