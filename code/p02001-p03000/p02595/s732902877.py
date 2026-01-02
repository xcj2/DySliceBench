#                               #
    # author : samars_diary #
    # 17-09-2020 │ 16:08:30 #
#                               #

import sys, os.path, math

#if(os.path.exists('input.txt')):
    #sys.stdin = open('input.txt',"r")
    #sys.stdout = open('output.txt',"w")

sys.setrecursionlimit(10 ** 5)

def mod(): return 10**9+7
def i(): return sys.stdin.readline().strip()
def ii(): return int(sys.stdin.readline())
def li(): return list(sys.stdin.readline().strip())
def mii(): return map(int, sys.stdin.readline().split())
def lii(): return list(map(int, sys.stdin.readline().strip().split()))

#print=sys.stdout.write

def solve():
    n,d=mii();c=0
    for _ in range(n):
        a,b=mii()
        if math.sqrt((a**2)+(b**2))<=d:
            c+=1
    print(c)
for _ in range(1):
    solve()