import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
sl = [S() for _ in range(N)]
#AC = WA = TLE = RE = 0
print('AC x '+ str(sl.count('AC')))
print('WA x '+ str(sl.count('WA')))
print('TLE x '+ str(sl.count('TLE')))
print('RE x '+ str(sl.count('RE')))