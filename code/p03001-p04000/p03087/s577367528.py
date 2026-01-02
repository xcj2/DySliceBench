import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,q = LI()
    s = "$" + S()

    lst = [0 for _ in range(n+1)]
    for i in range(n):
        before = s[i]
        after = s[i+1]
        if before == "A" and after == "C":
            lst[i+1] = lst[i] + 1
        else:
            lst[i+1] = lst[i]
    for _ in range(q):
        l,r = LI()
        ans = lst[r] - lst[l]
        print(ans)
main()