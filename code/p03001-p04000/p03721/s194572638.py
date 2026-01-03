import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, k = LI()
    lst = []

    for _ in range(n):
        a, b = LI()
        lst.append((a,b))
    
    lst.sort(key=lambda x: x[0])
    taken = 0
    ans = 0

    for i in range(n):
        ans = lst[i][0]
        taken += lst[i][1]

        if taken >= k:
            break

    print(ans)
main()
