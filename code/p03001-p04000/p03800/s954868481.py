from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

def check(x):
    res[0] = x[0]
    res[1] = x[1]
    for i in range(1,n-1):
        if (res[i] == 'S' and s[i] == 'o') or (res[i] == 'W' and s[i] == 'x'):
            if res[i-1] == 'S':
                res[i+1] = 'S'
            else:
                res[i+1] = 'W'
        else:
            if res[i-1] == 'S':
                res[i+1] = 'W'
            else:
                res[i+1] = 'S'
    # print(res)
    if (res[n-1] == 'S' and s[n-1] == 'o') or (res[n-1] == 'W' and s[n-1] == 'x'):
        if res[n-2] != res[0]:
            return False
    else:
        if res[n-2] == res[0]:
            return False
    if (res[0] == 'S' and s[0] == 'o') or (res[0] == 'W' and s[0] == 'x'):
        if res[n-1] != res[1]:
            return False
    else:
        if res[n-1] == res[1]:
            return False
    return res

n = inp()
s = input()
a = [['S','S'],['S','W'],['W','S'],['W','W']]
res = [''] * n
# print(a)
for i in range(4):
    if check(a[i]):
        print(''.join(res))
        quit()
print(-1)