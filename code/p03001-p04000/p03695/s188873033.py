import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    lst = [False]*8
    god = 0
    for i in a:
        rank = i//400
        if rank<=7:
            lst[rank] = True
        else:
            god += 1
    ans = lst.count(True)
    if ans == 0:
        ans = 1
        god -= 1

    print(ans,ans + god)

main()