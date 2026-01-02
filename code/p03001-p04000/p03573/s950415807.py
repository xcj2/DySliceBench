import bisect,collections,copy,heapq,itertools,math,string
import sys
def I():
    # 1 line 1 int
    return int(sys.stdin.readline().rstrip())
def LI():
    # 1 line n ints
    return list(map(int,sys.stdin.readline().rstrip().split()))
def S():
    # 1 line 1 string
    return sys.stdin.readline().rstrip()
def LS():
    # 1 line n strings
    return list(sys.stdin.readline().rstrip().split())
def println(s):
    print(f"{s}\n")

# https://atcoder.jp/contests/abc075/tasks/abc075_a
xs  = LI()

if xs[0] == xs[1]:
    println(xs[2])
elif xs[0] == xs[2]:
    println(xs[1])
else:
    println(xs[0])
