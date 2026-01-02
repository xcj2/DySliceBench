import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    n, m = LI()
    a = LI()
    lst = []

    for e in a:
        lst.append((e, 1))

    for _ in range(m):
        b, c = LI()
        lst.append((c, b))

    lst.sort(reverse=True)
    ans = 0
    cnt = 0

    for t in lst:
        time = min(t[1], n-cnt)
        ans += t[0]*time
        cnt += time
        if cnt == n:
            break
    
    print(ans)

        


main()
