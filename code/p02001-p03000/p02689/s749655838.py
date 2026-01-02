import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
n, m = M()
h_list = LI()
ans_list = [1] * n
for _ in range(m):
    a, b = M()
    if h_list[a-1] < h_list[b-1]:
        ans_list[a-1] = 0
    elif h_list[a-1] == h_list[b-1]:
        ans_list[a-1] = 0
        ans_list[b-1] = 0
    else:
        ans_list[b-1] = 0
print(sum(ans_list))