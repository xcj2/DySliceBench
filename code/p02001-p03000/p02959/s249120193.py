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
    ans = 0

    for i in range(n):
        tem = a[i]
        a[i] = max(0,a[i]-b[i])
        attack = tem-a[i]
        b[i] -= attack
        ans += attack

        tem = a[i+1]
        a[i+1] = max(0,a[i+1]-b[i])
        attack = tem-a[i+1]
        ans += attack
    
    print(ans)


main()
