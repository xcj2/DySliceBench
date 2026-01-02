import sys
sys.setrecursionlimit(10**9)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
n=INT()
a=["a" for i in range(n)]
def f(num):
    global n,a
    if num==n:
        print("".join([str(n) for n in a]))
        return
    elif num==1:
        a[num]="a"
        f(num+1)
        a[num]="b"
        f(num+1)
    else:
        a[num]="a"
        f(num+1)
        a[num]="b"
        f(num+1)
        try:
            if a.index("b")<num:
                a[num]="c"
                f(num+1)
            if a.index("c")<num:
                a[num]="d"
                f(num+1)
            if a.index("d")<num:
                a[num]="e"
                f(num+1)
            if a.index("e")<num:
                a[num]="f"
                f(num+1)
            if a.index("f")<num:
                a[num]="g"
                f(num+1)
            if a.index("g")<num:
                a[num]="h"
                f(num+1)
            if a.index("h")<num:
                a[num]="i"
                f(num+1)
            if a.index("i")<num:
                a[num]="j"
                f(num+1)
        except:
            pass
f(1)
    