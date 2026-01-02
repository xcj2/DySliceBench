import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    l = LI()
    l.sort()
    ans = 0

    for i in range(n):
        for j in range(i):
            mini = l[i] - l[j]
            if mini < l[j]:
                ans += n-bisect.bisect_right(l, mini) - (n-j)

    print(ans)

main()
