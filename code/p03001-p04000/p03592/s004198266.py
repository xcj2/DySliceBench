import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m, k = LI()
    for i in range(n):
        unit = n-2*i

        if unit == 0:
            if k == i*m:
                print("Yes")
                break
        else:
            j = (k-i*m)//(n-2*i)
            jr = (k-i*m)%(n-2*i)

            if 0 <= j <= m and jr == 0:
                print("Yes")
                break
    else:
        print("No")
main()
