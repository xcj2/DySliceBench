import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    v = LI()
    acnt = collections.Counter(v[::2])
    bcnt = collections.Counter(v[1::2])
    acnt = list(acnt.items())
    bcnt = list(bcnt.items())
    acnt.sort(key=lambda x: x[1], reverse=True)
    bcnt.sort(key=lambda x: x[1], reverse=True)

    ans = 0

    if len(acnt) == len(bcnt) == 1:
        if acnt[0][0] == bcnt[0][0]:
            ans = n//2
        else:
            ans = 0
    elif len(acnt)==1 or len(bcnt) == 1:
        if acnt[0][0] == bcnt[0][0]:
            if len(acnt) != 1:
                ans = n//2 - acnt[1][1]
            else:
                ans = n//2 - bcnt[1][1]
        else:
            ans = n//2 - min(acnt[0][1], bcnt[0][1])
    else:
        if acnt[0][0] == bcnt[0][0]:
            ans = n - acnt[0][1] - max(acnt[1][1], bcnt[1][1])
        else:
            ans = n - acnt[0][1]*2

    print(ans)

main()
