import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n,m = LI()
    s = [[] for i in range(n)]
    ans = 0
    for i in range(1,m+1):
        lst = LI()
        for j in lst[1:]:
            s[j-1].append(i)
    p = [0] + LI()
    # print(n,m,s,p)
    bits = itertools.product([0,1],repeat=n)
    for bit in bits:
        lst = [0 for _ in range(m+1)]
        for i in range(n):
            if bit[i] == 1:
                for j in s[i]:
                    lst[j] = not lst[j]
        if lst == p:
            ans+= 1
    print(ans)
main()