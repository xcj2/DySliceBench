import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    lst = [1 for i in range(10**5+5)]
    s = 1
    for i in range(3,10**5+5):
        s += lst[i-2]
        lst[i] = s
    n,m = LI()
    kaidan = [1 for _ in range(n+1)]
    for _ in range(m):
        a = I()
        kaidan[a] = 0
    itr = itertools.groupby(kaidan)
    span = []
    ans = 1

    for key, group in itr:
        lenth = len(list(group))
        if key == 0 and lenth >= 2:
            ans = 0
        elif key == 1:
            span.append(lenth)

    for i in span:
        ans *= lst[i]%1000000007
        ans %= 1000000007
    
    print(ans)

main()