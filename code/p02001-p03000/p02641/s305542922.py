import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
x, n = M()
if n == 0:
    print(x)
else:
    n_l = LI()
    suchi_list = [i for i in range(-300, 300)] # 1~100までのリスト
    ans = -1
    for i in n_l:
        suchi_list.remove(i)
    if x in suchi_list:
        ans = x
    else:
        for j in range(1, 101):
            if x-j in suchi_list:
                ans = x-j
            elif x+j in suchi_list:
                ans = x+j
            if ans != -1:
                break
    print(ans)