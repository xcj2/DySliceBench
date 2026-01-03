import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m = LI()
    cnt = [None] + [1 for _ in range(n)]
    exist = [False] + [False for _ in range(n)]
    exist[1] = True

    for _ in range(m):
        x, y = LI()

        cnt[y] += 1
        exist[y] |= exist[x]

        cnt[x] -= 1
        exist[x] &= cnt[x] != 0
    
    ans = sum(exist)
    print(ans)
main()
