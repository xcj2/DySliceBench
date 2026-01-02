import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m = LI()
    lst = []
    for _ in range(n):
        a, b = LI()
        lst.append([a,b])

    lst.sort()

    ans = 0
    for i in range(n):
        tem = lst[i][1]
        lst[i][1] = max(0, lst[i][1]-m)
        bought = tem-lst[i][1]
        m -= bought
        ans += lst[i][0]*bought
        if m == 0:
            break

    print(ans)   
main()
